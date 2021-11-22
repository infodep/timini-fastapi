from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import List, Dict

from bantre.system.group import groups_sections
from bantre.system.entity import EntityModel, entities_sections
from bantre.database import Base


class SectionModel(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=True)
    forum_priority = Column(Integer, nullable=False, default=0)
    # not a great name but denotes which groups have which permissions in this section
    groups_permissions = relationship('GroupModel', secondary=groups_sections,\
        back_populates = 'sections_permissions', lazy='dynamic')
    entities = relationship('EntityModel', secondary=entities_sections,
                               back_populates='sections')


# # Pydantic interfaces

# class Section(BaseModel):
#     id: int
#     name: str
#     forum_priority: int
#     groups_permissions: List[Dict[Group, Dict[str, bool]]]
#     entities: List[EntityModel]


# from bantre.system.group import Group
# Section.update_forward_refs()