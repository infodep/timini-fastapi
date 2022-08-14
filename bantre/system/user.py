from datetime import date, datetime
from enum import Enum
from os import link
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.sql.functions import func
from sqlmodel import Field, SQLModel
from sqlmodel.main import Relationship


if TYPE_CHECKING:
    from .group import Group


class ThemeName(str, Enum):
    light = "light"
    dark = "dark"


class UserConfigBase(SQLModel):
    forum_signature: str
    food_preferences: str
    card_no: str
    enable_pay_by_card: int


class UserConfig(UserConfigBase, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="config")


class UserGroupLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    group_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    start_time: Optional[datetime] = Field(
        sa_column_kwargs={"server_default": func.now()}
    )
    end_time: Optional[datetime] = Field(sa_column_kwargs={"default": datetime.max})


class UserBase(SQLModel):
    username: str
    email: str
    language: Optional[str] = "norwegian"
    timezone: Optional[str] = "Europe/Oslo"
    admin: Optional[bool] = False
    theme: Optional[ThemeName] = "light"


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    login_time: Optional[datetime] = Field(default=datetime.now())
    logout_time: Optional[datetime] = Field(default=datetime.now())
    deleted: Optional[bool] = False
    hidden: Optional[bool] = False
    last_activity: Optional[datetime] = Field(default=datetime.now())
    started_year: Optional[int] = Field(default=date.today().year)
    config: Optional[UserConfig] = Relationship(back_populates="user")
    groups: List["Group"] = Relationship(
        back_populates="members", link_model=UserGroupLink
    )
