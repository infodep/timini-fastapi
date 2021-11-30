from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import func

if TYPE_CHECKING:
    from .section import Section

class EntitySectionLink(SQLModel, table=True):
    entity_id: Optional[int] = Field(
        default=None, foreign_key="entity.id", primary_key= True
    )
    section_id: Optional[int] = Field(
        default=None, foreign_key="section.id", primary_key= True
    )


class EntityBase(SQLModel):
    module_id: int
    section_id: int
    
class Entity(EntityBase, table=True):
    """This is an actual database table because it has table=True"""
    id: Optional[int] = Field(default=None, primary_key=True)
    creator_id: int
    created: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now()})
    touched: Optional[datetime] = Field(sa_column_kwargs={"server_default": func.now(), "server_onupdate": func.now()})
    views: int
    sections: List["Section"] = Relationship(back_populates="entities", link_model=EntitySectionLink)
