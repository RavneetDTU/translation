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