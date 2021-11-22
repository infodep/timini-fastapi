from sqlalchemy import Column, Integer, DateTime, ForeignKey, Table
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from bantre.database import Base

entities_sections = Table('entities_sections',
    Base.metadata,
    Column('entity_id', Integer, ForeignKey('entities.id')),
    Column('section_id', Integer, ForeignKey('sections.id'))
)


class EntityModel(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=True,
                        server_default=func.now())
    touched = Column(DateTime, nullable=True,
                        server_default=func.now(), server_onupdate=func.now())
    creator_id = Column(Integer, nullable=False)
    section_id = Column(Integer, nullable=False)
    views = Column(Integer, nullable=False, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'entity',
        'polymorphic_on': module_id
    }

    sections = relationship('SectionModel', secondary=entities_sections,
                               back_populates='entities')
