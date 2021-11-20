from sqlalchemy import Column, String, Integer, BigInteger, Text, Float

from common.sql_alchemy.base import Base


class Translation(Base):
    __tablename__ = "translation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    input_language = Column(String(50))
    output_language = Column(String(50))
    input_text = Column(Text)
    translated_text = Column(Text)
    confidence_score = Column(Float)
    created_on = Column(BigInteger, nullable=False)
