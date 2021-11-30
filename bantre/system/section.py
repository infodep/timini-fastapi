from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

from .entity import EntitySectionLink
from .group import GroupSectionLink

if TYPE_CHECKING:
    from .entity import Entity
    from .group import Group


class SectionBase(SQLModel):
    name: str
    forum_priority: int

class Section(SectionBase, table=True):
    """This is an actual database table because it has table=True"""
    id: Optional[int] = Field(default=None, primary_key=True)
    
    groups_permissions: List["Group"] = Relationship(back_populates="sections_permissions", link_model=GroupSectionLink)
    entities: List["Entity"] = Relationship(back_populates="sections", link_model=EntitySectionLink)