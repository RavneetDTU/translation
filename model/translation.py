from sqlalchemy import Column, String, Integer, BigInteger, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

from common.sql_alchemy.base import Base
from model.auth import User


class Translation(Base):
    __tablename__ = "translation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    input_language = Column(String(50))
    output_language = Column(String(50))
    input_text = Column(Text)
    translated_text = Column(Text)
    confidence_score = Column(Float)
    created_on = Column(BigInteger, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", name="fk_translation_user_id"), nullable=False)
    suggestion = relationship("Suggestion", backref=backref("translation", cascade="all"))


class TranslationHandler(Base):
    __tablename__ = "translation_handler"
    id = Column(Integer, primary_key=True, autoincrement=True)
    input_language = Column(String(50))
    output_language = Column(String(50))
    handler = Column(String(50))


class Suggestion(Base):
    __tablename__ = "suggestion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    suggested_text = Column(Text, nullable=False)
    translation_id = Column(Integer, ForeignKey('translation.id'), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", name="fk_suggestion_user_id"), nullable=False)
