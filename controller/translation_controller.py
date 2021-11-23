from pinject import inject
from sqlalchemy import and_

from common.pinject.container import Container
from config.config import MySQLSettings
from controller.ai_controller import AIController
from model.translation import Translation, TranslationHandler, Suggestion


class TranslationController:

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service
        Container(MySQLSettings.get_settings())
        container = Container.get_object_graph()
        self.__ai_controller = container.provide(AIController)

    def get_translation(self, translate_data):
        translation_dict = translate_data.dict()
        db_session = self.__mysql_alchemy_session_service.get_session()
        if translation_dict.get("input_language", None) is None:
            translation_dict['input_language'] = self.__ai_controller.language_detection(translation_dict['input_text'])
        translation_handler = self.__get_translation_handler(translation_dict['input_language'],
                                                             translation_dict['output_language'])
        if translation_handler is None:
            output_text = self.__translate_using_intermediate_handler(translation_dict['input_text'],
                                                                      translation_dict['input_language'],
                                                                      translation_dict['output_language'])
        else:
            handler = self.__ai_controller.ai_strategies.get(translation_handler.handler)
            output_text = handler(translation_dict['input_text'])
        translation_dict.update({
            "translated_text": output_text,
            "confidence_score": 0,
            "created_on": 1
        })
        translate_obj = Translation(**translation_dict)
        db_session.add(translate_obj)
        db_session.flush()
        db_session.commit()
        translation_dict.update({
            "translation_id": translate_obj.id
        })
        return translation_dict

    def __translate_using_intermediate_handler(self, input_text, input_language, output_language):
        db_session = self.__mysql_alchemy_session_service.get_session()
        handlers_starting_with_input_language = db_session.query(TranslationHandler).filter(
            TranslationHandler.input_language == input_language).all()
        for intermediate_handler in handlers_starting_with_input_language:
            translation_handler = self.__get_translation_handler(intermediate_handler.output_language, output_language)
            if translation_handler:
                intermediate_handler_strategy = self.__ai_controller.ai_strategies.get(intermediate_handler.handler)
                intermediate_text = intermediate_handler_strategy(input_text)
                translation_handler_strategy = self.__ai_controller.ai_strategies.get(translation_handler.handler)
                output_text = translation_handler_strategy(intermediate_text)
                return output_text
        return None

    def __get_translation_handler(self, input_language, output_language):
        return self.__mysql_alchemy_session_service.get_session().query(TranslationHandler).filter(
            and_(TranslationHandler.input_language == input_language,
                 TranslationHandler.output_language == output_language)).first()

    def add_suggestion(self, suggestion):
        db_session = self.__mysql_alchemy_session_service.get_session()
        translation = self.__get_translation_by_id(suggestion.translation_id)
        if translation is None:
            return "Invalid Translation id %s" % suggestion.translation_id
        suggestion_dict = suggestion.dict()
        suggestion_obj = Suggestion(**suggestion_dict)
        db_session.add(suggestion_obj)
        db_session.flush()
        db_session.commit()
        return None

    def __get_translation_by_id(self, translation_id: int):
        translation = self.__mysql_alchemy_session_service.get_session().query(Translation).filter(
            Translation.id == translation_id).first()
        return translation
