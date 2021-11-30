from sqlmodel import SQLModel, create_engine, Session

# import all SQLModels which are tables in the database
from bantre.system.entity import Entity
from bantre.system.group import Group
from bantre.system.section import Section
from bantre.system.user import User, UserConfig

SQLALCHEMY_DATABASE_URL = "mysql://root:timini@db/timini"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True #Remember to turn this off when going to prod
)

def get_db():
    with Session(engine) as db:
        try:
            yield db
        finally:
            db.close()

def create_db_and_tables():
    """Only for testing"""
    SQLModel.metadata.create_all(engine)
