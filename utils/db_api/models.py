from sqlalchemy import (
    Column, BigInteger, 
    String)

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    first_name = Column(String(50))