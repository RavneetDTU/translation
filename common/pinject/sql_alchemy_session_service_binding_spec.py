from pinject import BindingSpec

from common.sql_alchemy.sql_alchemy_session_service import MysqlAlchemySessionService


class SQLAlchemyBindingSpec(BindingSpec):

    def __init__(self, config):
        self.__config = config

    def configure(self, bind):
        pass

    def provide_mysql_alchemy_session_service(self):
        return MysqlAlchemySessionService(self.__config)
