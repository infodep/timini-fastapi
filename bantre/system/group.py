from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.orm import relationship
from enum import Enum
from typing import ForwardRef, List, Dict

from bantre.system.user import users_groups
from bantre.database import Base

# Relational table between groups and sections
groups_sections = Table(
    "groups_sections",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("section_id", Integer, ForeignKey("sections.id")),
    Column("read", TINYINT(1), default=0, index=True),
    Column("write", TINYINT(1), default=0),
    Column("admin", TINYINT(1), default=0),
)


class GroupModel(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    type = Column(TINYINT(2), nullable=False, default=None)
    description = Column(String(255), nullable=False, default=None)
    members = relationship("UserModel", secondary=users_groups, back_populates="groups")
    sections_permissions = relationship(
        "SectionModel",
        secondary=groups_sections,
        back_populates="groups_permissions",
        lazy="dynamic",
    )


# # Pydantic interfaces
# class Permission(str, Enum):
#     read = "read"
#     write = "write"
#     admin = "admin"

# class Group(BaseModel):
#     id: int
#     name: str
#     type: int
#     description: str
#     members: List["User"]
#     sections_permissions: List[Dict[Section, Dict[str, bool]]]


# from bantre.system.user import User
# from bantre.system.section import Section
# Group.update_forward_refs()
