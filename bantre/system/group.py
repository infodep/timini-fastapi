from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

from .user import UserGroupLink

if TYPE_CHECKING:
    from .section import Section
    from .user import User

class GroupSectionLink(SQLModel, table=True):
    group_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key= True
    )
    section_id: Optional[int] = Field(
        default=None, foreign_key="section.id", primary_key= True
    )
    read: Optional[bool] = Field(default=False, index=True)
    write: Optional[bool] = Field(default=False)
    admin: Optional[bool] = Field(default=False)

class GroupBase(SQLModel):
    name: str
    type: int
    description: str

class Group(GroupBase, table=True):
    """This is an actual database table because it has table=True"""
    id: Optional[int] = Field(default=None, primary_key=True)
    members: List["User"] = Relationship(back_populates="groups", link_model=UserGroupLink)
    sections_permissions: List["Section"] = Relationship(back_populates="groups_permissions", link_model=GroupSectionLink)
