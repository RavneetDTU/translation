import datetime

from jose import jwt, JWTError
from passlib.context import CryptContext
from pinject import inject

from common.pinject.container import Container
from common.pinject.sql_alchemy_session_service_provider import SqlAlchemySessionServiceProvider
from config.config import Settings
from model.auth import User, Role

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename= 'all_logs.log',  #filename='%slog' % __file__[:-2],
    filemode='a'
)

logfile = 'auth_controller.py'


class AuthController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @inject()
    def __init__(self):
        Container(Settings.get_settings())
        container = Container.get_object_graph()
        self.__sql_alchemy_session_service_provider = container.provide(SqlAlchemySessionServiceProvider)
        self.__config = Settings.get_settings()

    def register_user(self, user_data):
        db_session = self.__sql_alchemy_session_service_provider.session()
        user_dict = user_data.dict()
        existing_user = self.__get_user_by_email(user_dict["email"])
        if existing_user:
            logging.info(logfile+' register_user func : username already exists')
            return "User with email id %s already exists" % user_dict["email"]
        user_dict.update({
            "role": Role.CUSTOMER.value,
            "created_on": 1,
            "modified_on": 1
        })
        user_dict.update({
            "password": self.__get_password_hash(user_dict["password"])
        })
        user_obj = User(**user_dict)
        db_session.add(user_obj)
        db_session.flush()
        return None

    def __get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def __get_user_by_email(self, email):
        return self.__sql_alchemy_session_service_provider.session().query(User).filter(User.email == email).first()

    def login_user(self, form_data):
        user, error = self.authenticate_user(form_data.username, form_data.password)
        if error:
            logging.error(logfile+' login_user func : Error found in login_user %s' % error)
            return None, error
        access_token = self.__create_access_token(user)
        return {"access_token": access_token, "token_type": "bearer"}, None

    def authenticate_user(self, username: str, password: str):
        user = self.__get_user_by_email(username)
        if not user:
            logging.error(logfile+' authenticate_user func : Invalid Username %s' % username)
            return None, "Invalid user name %s" % username
        if not self.verify_password(password, user.password):
            logging.error(logfile+' authenticate_user func : Invalid password')
            return None, "Invalid password"
        return user, None

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def __create_access_token(self, data):
        payload = {
            "sub": data.email,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=self.__config.jwt.access_token_expire_days)
        }
        encoded_jwt = jwt.encode(payload, self.__config.jwt.secret_key, algorithm=self.__config.jwt.algorithm)
        logging.info(logfile+' __create_access_token func: encoded_jwt has been generated')
        return encoded_jwt

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.__config.jwt.secret_key, algorithms=[self.__config.jwt.algorithm])
            username: str = payload.get("sub")
            if username is None:
                logging.error(logfile+' username not found, hence raising JWTerror')
                raise JWTError
            user = self.__get_user_by_email(username)
            return User.get_user_data(user), None
        except JWTError as e:
            logging.error(logfile+' JWTError %s' % e)
            return None, e.args[0].args[0]

    def get_user_by_user_id(self, user_id):
        logging.info(logfile+' user info generated successfully using user_id')
        return self.__sql_alchemy_session_service_provider.session().query(User).filter(User.id == user_id).first()
