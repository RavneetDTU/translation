from pinject import inject
from common.pinject.container import Container
from config.config import MySQLSettings
from model.translation import Translation


class TranslationController:

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service

    def getTranslation(self, translate_data):
        translation_dict = translate_data.dict()
        translation_dict.update({
            "translated_text": "translated_text",
            "confidence_score": 4.0,
            "created_on": 1
        })
        translate_obj = Translation(**translation_dict)
        db_session = self.__mysql_alchemy_session_service.get_session()
        db_session.add(translate_obj)
        db_session.flush()
        # db_session.commit()
        return translation_dict

