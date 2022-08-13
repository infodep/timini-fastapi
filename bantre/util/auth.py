from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import Null

from bantre.system.user import User, UserInDB, UserModel
from bantre.util import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_uid(db: Session, id: int):
    return db.query(UserModel).filter(UserModel.id == id).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def decode_token(
    db: Session, token: str, settings: config.Settings = Depends(config.get_settings)
) -> User:
    try:
        payload = jwt.decode(token, settings.access_token_key)
    except JWTError:
        return None
    # TODO: Cont
    print(payload)
    return User(id=1, username="test", groups={1: "tiministene"})


def token_required(token: str = Depends(oauth2_scheme)) -> User:
    user = decode_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def token_optional(token: str = Depends(oauth2_scheme)) -> User | None:
    """
    This function is like token_required, but returns the anonymous user if not validated.
    It is very important to make sure that the front end makes sure it is logged in so that we dont make a bunch of db entries as the anonymous user
    """
    user = decode_token(token)
    if user is None:
        user = User(id=-1, username="Anonymous", admin=False, email=Null)
    return user


def create_access_token(
    id: int,
    expires_delta=Optional[datetime],
    settings: config.Settings = Depends(config.get_settings),
):
    to_encode = {
        "id": id,
        "token_type": "access_token",
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(settings.access_token_lifetime)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.access_token_key, algorithm=settings.jwt_algorithm
    )
    return encoded_jwt


def create_refresh_token(
    id: int,
    expires_delta=Optional[datetime],
    settings: config.Settings = Depends(config.get_settings),
):
    to_encode = {
        "id": id,
        "token_type": "refresh_token",
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(settings.access_token_lifetime)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.refresh_token_key, algorithm=settings.jwt_algorithm
    )
    return encoded_jwt
