from sqlalchemy import (
    Column, BigInteger, 
    String, Integer, Text)

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    first_name = Column(String(50))


class Channel(Base):
    __tablename__ = "channel"

    chat_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    title = Column(String(150))


class Audio(Base):
    __tablename__ = "audio"

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger)
    text = Column(Text)
    distination = Column(String(150))


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    username = Column(String(150))
    password = Column(String(150))
