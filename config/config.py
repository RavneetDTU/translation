from functools import lru_cache

from pydantic import BaseSettings


class MySQLSettings(BaseSettings):
    user_name: str = "translator"
    password: str = "translator#123"
    host: str = "localhost"
    port: int = 3306
    database: str = "translation"


    @staticmethod
    @lru_cache()
    def get_settings():
        return MySQLSettings()


class JWTSettings(BaseSettings):
    secret_key: str = "d3a7f94bc015829ed9bb2b6634cb0637e5e3988591107b664185bff5efd40200"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1

    @staticmethod
    @lru_cache()
    def get_settings():
        return JWTSettings()


class Settings(BaseSettings):
    mysql = MySQLSettings.get_settings()
    jwt = JWTSettings.get_settings()

    @staticmethod
    @lru_cache()
    def get_settings():
        return Settings()