from sqlalchemy import Column, Integer, DateTime, ForeignKey, Table, String, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARBINARY, TINYINT
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, ForwardRef
from pydantic import BaseModel

from bantre.database import Base

# These are database models

#Relational table between users and groups
users_groups = Table('users_groups',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('start_time', DateTime, server_default=func.now()),
    Column('end_time', DateTime, default=datetime.max)
)
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), nullable=False, unique=True)
    password = Column(VARBINARY(60), nullable=True)
    email = Column(String(255), nullable=True)
    language = Column(String(50), nullable=False, default="english")
    timezone = Column(String(50), nullable=False, default="Europe/Oslo")
    last_activity = Column(INTEGER(unsigned=True),
                              nullable=False, default=0)
    login_time = Column(DateTime, nullable=True)
    logout_time = Column(DateTime, nullable=True)
    status = Column(TINYINT(1), default=1)
    hidden = Column(TINYINT(1), default=0)
    started_year = Column(Integer, default=None)
    theme = Column(String(50), default="light")

    # These are imaginary columns that link the tables together
    groups = relationship('GroupModel', secondary=users_groups, back_populates = 'members') 
    config = relationship('UserConfigModel', back_populates="user", uselist=False) # useList=False makes this a one-to-one relationship

class UserConfigModel(Base):
    __tablename__ = 'users_config'
    uid = Column(Integer, ForeignKey('users.id'), primary_key=True, autoincrement=False)
    forum_signature = Column(Text(), nullable=False, default="")
    food_preferences = Column(Text(), nullable=False, default="")
    card_no = Column(VARBINARY(50), nullable=True)
    enable_pay_by_card = Column(TINYINT(1), nullable=False, default=False)

    # imaginary column that connects to the UserModel
    user = relationship('UserModel', back_populates="config", uselist=False)


# The following are pydantic interfaces used for packaging data
class ThemeName(str, Enum):
    light = "light"
    dark = "dark"

class Times(str, Enum):
    start_time = "start_time"
    end_time = "end_time"

class UserConfig(BaseModel):
    forum_signature: str
    food_preferences: str
    card_no: str
    enable_pay_by_card: int

class User(BaseModel):
    id: int
    username: str
    email: str
    language: str
    timezone: str
    last_activity: int
    login_time: datetime
    logout_time: datetime
    status: bool
    hidden: bool
    started_year: int
    # groups: List[Dict["Group", Dict[Times, datetime]]]
    config: UserConfig
    admin: Optional[bool] = False
    theme: Optional[ThemeName] = "light"

class UserInDB(User):
    password: str

# from bantre.system.group import Group
# User.update_forward_refs()