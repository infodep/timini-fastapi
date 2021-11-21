from bantre.system.entity import EntityModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text


class ArticleModel(EntityModel):
    __tablename__ = 'mod_article'
    # This will be the value of module_id column in entities table
    __mapper_args__ = {'polymorphic_identity': 4}
    id = Column('entity_id', Integer, ForeignKey(
        'entities.id'), primary_key=True)
    title = Column(String(64), nullable=False)
    text = Column(Text(), nullable=False)
    text_source = Column(Text(), nullable=False)
    image = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Article(title={self.title}, text={self.text}, text_source={self.text_source}, image={self.image})"
