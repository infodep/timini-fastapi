import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql://root:timini@db/timini"

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=metadata)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
