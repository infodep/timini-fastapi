from sqlalchemy import Column, Integer
from bantre.database import Base

class TokenModel(Base):
    __tablename__ = "refresh_tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    # TODO: add field that distinguishes tokens so that you can log out of only one device at a time