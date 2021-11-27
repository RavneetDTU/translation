from pinject import inject
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class MysqlAlchemySessionService:

    def __init__(self, config):
        super().__init__()
        self.__config = config
        self.__Session = None
        self.__engine = None
        db_config = self.__config
        db_config = (db_config['mysql'].user_name,
                     db_config['mysql'].password,
                     db_config['mysql'].host,
                     db_config['mysql'].port,
                     db_config['mysql'].database)
        self.__connection_string = "mysql+mysqlconnector://%s:%s@%s:%d/%s" % db_config

    def connection_string(self):
        return self.__connection_string

    def get_engine(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)

        return self.__engine

    def get_session(self) -> Session:
        if self.__Session is None:
            self.__Session = sessionmaker(bind=self.get_engine())

        return self.__Session()
