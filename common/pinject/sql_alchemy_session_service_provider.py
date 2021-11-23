from pinject import inject
from sqlalchemy.orm import Session


class SqlAlchemySessionServiceProvider:
    __connections = {}

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service

    def session(self) -> Session:
        return self.__mysql_alchemy_session_service.get_session()

    def connection_string(self):
        return self.__mysql_alchemy_session_service.connection_string()

