from pinject import inject
from common.pinject.container import Container
from config.config import MySQLSettings
from model.translation import Translation


class TranslationController:

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service
        # Container(MySQLSettings.get_settings())
        # container = Container.get_object_graph()
        # self.__sql_alchemy_session_service_provider = container.provide(SqlAlchemySessionServiceProvider)

    def getTranslation(self):
        print("fdsfds")
        x = self.__mysql_alchemy_session_service.get_session().query(Translation).all()
        print(x)
        pass

