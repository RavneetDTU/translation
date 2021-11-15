from common.sql_alchemy.base import Base
from sqlalchemy import Column, String, Integer, BigInteger, JSON, ForeignKey, Enum


class Translation(Base):
    __tablename__ = "translation"
    id = Column(Integer, primary_key=True, autoincrement=True)
