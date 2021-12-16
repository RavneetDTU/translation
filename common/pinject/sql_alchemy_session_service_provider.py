from pinject import inject
from sqlalchemy.orm import Session


class SqlAlchemySessionServiceProvider:
    __session = None

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service

    def session(self) -> Session:
        if SqlAlchemySessionServiceProvider.__session is None:
            SqlAlchemySessionServiceProvider.__session = self.__mysql_alchemy_session_service.get_session()
        return SqlAlchemySessionServiceProvider.__session

    def connection_string(self):
        return self.__mysql_alchemy_session_service.connection_string()

