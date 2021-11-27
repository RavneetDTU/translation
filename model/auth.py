import enum

from sqlalchemy import Column, String, Integer, BigInteger, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from common.sql_alchemy.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    role = Column(String(256), nullable=False)
    created_on = Column(BigInteger, nullable=False)
    modified_on = Column(BigInteger, nullable=False)
    translation = relationship("Translation", backref=backref("user", cascade="all"))
    suggestion = relationship("Suggestion", backref=backref("user", cascade="all"))

    def __repr__(self):
        return "<User(user_id='%d', email='%s', name='%s, created_on=%s, modified_on=%s')>" % (
            self.id, self.email, self.name, self.created_on, self.modified_on)

    @staticmethod
    def get_user_data(user):
        return {
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }


class Role(enum.Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
