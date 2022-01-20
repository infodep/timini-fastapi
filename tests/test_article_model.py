from sqlmodel import Session
from bantre.modules.article.article_model import Article
from .conftest import session_fixture, client_fixture

from bantre.system.user import User
from bantre.system.section import Section
from bantre.system.entity import Entity

def test_article_orm(session: Session):
    post_user = User(
        username="bucky",
        email="ricky@bucky.com",
        password="timini"
    )
    post_section = Section(
        name="test_section",
        description="section made for test",
    )
    article_entity = Entity(creator=post_user, main_section=post_section, sections=[post_section])
    post_article = Article(
        title="Test Article",
        text="<p>This is a short article used for testing</p>",
        text_source="This is a short article used for testing",
        image=None,
        entity=article_entity
    )

    session.add(post_user)
    session.add(post_section)
    session.add(article_entity)
    session.add(post_article)
    session.commit()

    assert post_article.id is not None

    entity_from_db = session.get(Entity, post_article.id)
    assert entity_from_db.creator == post_article.entity.creator