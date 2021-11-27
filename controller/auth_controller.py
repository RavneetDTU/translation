import datetime
from jose import jwt, JWTError
from passlib.context import CryptContext
from pinject import inject

from config.config import Settings
from model.auth import User, Role


class AuthController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @inject()
    def __init__(self, mysql_alchemy_session_service):
        self.__mysql_alchemy_session_service = mysql_alchemy_session_service
        self.__config = Settings.get_settings()

    def register_user(self, user_data):
        db_session = self.__mysql_alchemy_session_service.get_session()
        user_dict = user_data.dict()
        existing_user = self.__get_user_by_email(user_dict["email"])
        if existing_user:
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
        db_session.commit()
        return None

    def __get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def __get_user_by_email(self, email):
        return self.__mysql_alchemy_session_service.get_session().query(User).filter(User.email == email).first()

    def login_user(self, form_data):
        user, error = self.authenticate_user(form_data.username, form_data.password)
        if error:
            return None, error
        access_token = self.__create_access_token(user)
        return {"access_token": access_token, "token_type": "bearer"}, None

    def authenticate_user(self, username: str, password: str):
        user = self.__get_user_by_email(username)
        if not user:
            return None, "Invalid user name %s" % username
        if not self.verify_password(password, user.password):
            return None, "Invalid password"
        return user, None

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def __create_access_token(self, data):
        payload = {
            "sub": data.email,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=self.__config.jwt.access_token_expire_minutes)
        }
        encoded_jwt = jwt.encode(payload, self.__config.jwt.secret_key, algorithm=self.__config.jwt.algorithm)
        return encoded_jwt

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.__config.jwt.secret_key, algorithms=[self.__config.jwt.algorithm])
            username: str = payload.get("sub")
            if username is None:
                raise JWTError
            user = self.__get_user_by_email(username)
            return User.get_user_data(user), None
        except JWTError as e:
            return None, e.args[0]