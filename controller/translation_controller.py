from pinject import inject
from sqlalchemy import and_

import utils
from common.pinject.container import Container
from common.pinject.sql_alchemy_session_service_provider import SqlAlchemySessionServiceProvider
from config.config import Settings
from controller.ai_controller import AIController
from controller.auth_controller import AuthController
from model.translation import Translation, TranslationHandler, Suggestion, LanguageHelper

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)

class TranslationController:

    @inject()
    def __init__(self):
        Container(Settings.get_settings())
        container = Container.get_object_graph()
        self.__sql_alchemy_session_service_provider = container.provide(SqlAlchemySessionServiceProvider)
        self.__ai_controller = container.provide(AIController)
        self.__auth_controller = container.provide(AuthController)

    def __translate(self, input_text, input_language, output_language):
        translation_handler = self.__get_translation_handler(input_language, output_language)
        error = None
        if translation_handler is None:
            output_text, error = self.__translate_using_intermediate_handler(input_text,
                                                                             input_language,
                                                                             output_language)
            logging.error('error in __translate function')
        else:
            handler = self.__ai_controller.ai_strategies.get(translation_handler.handler)
            output_text = handler(input_text)
        return output_text, error

    def get_translation(self, translate_data, user):
        translation_dict = translate_data.dict()
        db_session = self.__sql_alchemy_session_service_provider.session()
        language_helper = self.__get_language_helper(translation_dict["output_language"])
        if language_helper is None:
            logging.error('error in get_translation function, Invalid output language%s' % translation_dict["output_language"])
            return None, "Invalid output language %s" % translation_dict["output_language"]

        if translation_dict.get("input_language"):
            language_helper = self.__get_language_helper(translation_dict["input_language"])
            if language_helper is None:
                logging.error('error in get_translation function, Invalid input language %s' % translation_dict["input_language"])
                return None, "Invalid input language %s" % translation_dict["input_language"]
        if translation_dict.get("input_language", None) is None:
            translation_dict['input_language'] = self.__ai_controller.language_detection(translation_dict['input_text'])
            language_helper = self.__get_language_helper(translation_dict["input_language"])
            if language_helper is None:
                logging.error('error in get_translation function, Invalid input language %s detected' % translation_dict["input_language"])
                return None, "Invalid input language %s detected" % translation_dict["input_language"]
        output_text, error = self.__translate(translation_dict['input_text'], translation_dict['input_language'],
                                              translation_dict['output_language'])
        if error:
            logging.error('error in get_translation function, line no 54 i.e. %s' % error )
            return None, error
        translation_dict.update({
            "translated_text": output_text,
            "confidence_score": 0,
            "created_on": int(utils.current_timestamp()),
            "user_id": user["user_id"]
        })
        translate_obj = Translation(**translation_dict)
        db_session.add(translate_obj)
        db_session.flush()
        translation_dict.update({
            "translation_id": translate_obj.id
        })
        return translation_dict, None

    def __translate_using_intermediate_handler(self, input_text, input_language, output_language):
        db_session = self.__sql_alchemy_session_service_provider.session()
        handlers_starting_with_input_language = db_session.query(TranslationHandler).filter(
            TranslationHandler.input_language == input_language).all()
        for intermediate_handler in handlers_starting_with_input_language:
            translation_handler = self.__get_translation_handler(intermediate_handler.output_language, output_language)
            if translation_handler:
                intermediate_handler_strategy = self.__ai_controller.ai_strategies.get(intermediate_handler.handler)
                intermediate_text = intermediate_handler_strategy(input_text)
                translation_handler_strategy = self.__ai_controller.ai_strategies.get(translation_handler.handler)
                output_text = translation_handler_strategy(intermediate_text)
                return output_text, None
        logging.error('Cannot translate from %s to %s' % (input_language, output_language))
        return None, "Cannot translate from %s to %s" % (input_language, output_language)

    def __get_translation_handler(self, input_language, output_language):
        return self.__sql_alchemy_session_service_provider.session().query(TranslationHandler).filter(
            and_(TranslationHandler.input_language == input_language,
                 TranslationHandler.output_language == output_language)).first()

    def add_suggestion(self, suggestion, user_data):
        db_session = self.__sql_alchemy_session_service_provider.session()
        translation = self.__get_translation_by_id(suggestion.translation_id)
        if translation is None:
            logging.error('error in add_suggestion function, Invalid Translation ID %s' % suggestion.translation_id)
            return "Invalid Translation id %s" % suggestion.translation_id
        suggestion_dict = suggestion.dict()
        suggestion_dict.update({
            "user_id": user_data["user_id"]
        })
        suggestion_obj = Suggestion(**suggestion_dict)
        db_session.add(suggestion_obj)
        db_session.flush()
        logging.info('add_suggestion function worked perfectly fine')
        return None

    def __get_translation_by_id(self, translation_id: int):
        translation = self.__sql_alchemy_session_service_provider.session().query(Translation).filter(
            Translation.id == translation_id).first()
        logging.info('__get_translation_by_id function is working fine')
        return translation

    def __get_all_translation_by_input_output_language(self, input_language, output_language, start_time, end_time):
        translations = self.__sql_alchemy_session_service_provider.session().query(Translation).filter(
            and_(Translation.input_language == input_language, Translation.output_language == output_language,
                 Translation.created_on >= start_time, Translation.created_on <= end_time)).all()
        logging.info('__get_all_translation_by_input_output_language is working fine')
        return translations

    def __get_all_translation_by_user_id(self, user_id, start_time, end_time):
        translations = self.__sql_alchemy_session_service_provider.session().query(Translation).filter(
            and_(Translation.user_id == user_id, Translation.created_on >= start_time,
                 Translation.created_on <= end_time)).all()
        logging.info('__get_all_translation_by_user_id is working fine')
        return translations

    def get_translated_characters_by_input_output_language(self, input_language, output_language, start_time, end_time):
        if start_time > end_time:
            logging.info('Start time must be less than end time')
            return None, "Start time must be less than end time"
        language_helper = self.__get_language_helper(output_language)
        if language_helper is None:
            logging.error('Invalid output language %s in get_translated_characters_by_input_output_language' % output_language)
            return None, "Invalid output language %s" % output_language
        language_helper = self.__get_language_helper(input_language)
        if language_helper is None:
            logging.error('Invalid input language %s in get_translated_characters_by_input_output_language' % input_language)
            return None, "Invalid input language %s" % input_language
        translations = self.__get_all_translation_by_input_output_language(input_language, output_language, start_time, end_time)
        if not translations:
            logging.info('Translation not found with input language %s and output language %s in requested time range' % (
                input_language, output_language))
            return None, "Translation not found with input language %s and output language %s in requested time range" % (
                input_language, output_language)
        count = 0
        for translation in translations:
            count += len(translation.translated_text)
        return {
                   "characters_translated": count
               }, None

    def get_translated_characters_by_user_id(self, user_id, start_time, end_time):
        if start_time > end_time:
            logging.info('Start time must be less than end time')
            return None, "Start time must be less than end time"
        user = self.__auth_controller.get_user_by_user_id(user_id)
        if not user:
            logging.error('Invalid user id in get_translated_characters_by_user_id function  %s' % user_id)
            return None, "Invalid user id %s" % user_id
        translations = self.__get_all_translation_by_user_id(user_id, start_time, end_time)
        count = 0
        for translation in translations:
            count += len(translation.translated_text)
        return {
                   "characters_translated": count
               }, None

    def __get_language_helper(self, language):
        return self.__sql_alchemy_session_service_provider.session().query(LanguageHelper).filter(
            LanguageHelper.language == language).first()

    def get_model_status(self, input_language, output_language):
        language_helper = self.__get_language_helper(output_language)
        if language_helper is None:
            logging.error('Invalid output language error in get_model_status function  %s' % output_language)
            return None, "Invalid output language %s" % output_language
        language_helper = self.__get_language_helper(input_language)
        if language_helper is None:
            logging.error('Invalid input language error in get_model_status function %s' % input_language)
            return None, "Invalid input language %s" % input_language
        output_text, error = self.__translate(language_helper.sample_text, input_language, output_language)
        if output_text:
            return {
                "status": "active"
            }, None
        else:
            return {
                "status": "inactive"
            }, None
