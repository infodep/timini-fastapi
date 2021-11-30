import pytest 
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool

from bantre.app import app
from bantre.database import get_db
from bantre.system.user import User

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_db_override():
        return session
    
    app.dependency_overrides[get_db] = get_db_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_user_orm(session: Session):
    # Create user using the orm
    post_user = User(
        username="bucky",
        email="ricky@bucky.com",
        password="timini"
    )
    session.add(post_user)
    session.commit()
    session.refresh(post_user)
    # Assert that the posted user now has an id
    assert post_user.id is not None

    # Get the same user from the orm
    get_user = session.get(User, post_user.id)
    assert get_user.id == post_user.id
    assert get_user.username == "bucky"
    assert get_user.password == "timini"
    assert get_user.email == "ricky@bucky.com"

# def test_create_user(client: TestClient): # Navnene på variablene må være det samme som står i pytest.fixture dekoratorene
#     # This will be boilerplate for running tests using endpoints
#     # Create user 
#     response = client.post(
#         "/v1/users", json= {
#             "username": "bucky",
#             "name": "Richard-Andre Hewlett Buckminister Fuller",
#             "email": "ricky@bucky.com",
#             "private_email": "ladiesman@gmail.com",
#             "birthday": "2006-09-10",
#             "phone": "12345678"
#         }
#     )
#     data = response.json()

#     # Assert that he is equal to the one that we created
#     assert response.status_code == 200
#     assert data["name"] == "Richard-Andre Hewlett Buckminister Fuller"
#     assert data["email"] == "ricky@bucky.com"
#     assert data["private-email"] == "ladiesman@gmail.com"
#     assert data["birthday"] == "2006-09-10"
    