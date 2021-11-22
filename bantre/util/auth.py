from datetime import datetime, timedelta
from functools import wraps
from typing import Optional
import jwt

from bantre.system.user import UserModel, User, UserInDB
from bantre.util import config

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
def hash_password(password: str) -> str:
    return CryptContext.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return CryptContext.verify(plain_password, hashed_password)

def get_user_by_username(db: Session, username: str) -> UserInDB:
    return db.query(UserModel).filter(UserModel.username == username).first()

def get_user_by_uid(db: Session, id: int) -> UserInDB:
    return db.query(UserModel).filter(UserModel.id == id).first()

def authenticate_user(db: Session, username: str, password: str) -> bool|User:
    user = get_user_by_username(username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def decode_token(db: Session, token: str) -> User:  


    return User(
        id=1,  
        username="test",
        groups = {1: "tiministene"}
        )

async def token_required(token: str = Depends(oauth2_scheme)) -> User:
    user = decode_token(token)
    if user == None:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    return user

async def token_optional(token: str = Depends(oauth2_scheme)) -> User:
    user = decode_token(token)
    return user

def create_access_token(id: int, expires_delta = Optional[datetime], settings: config.Settings = Depends(config.get_settings)):
    to_encode = {
        "id": id,
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(settings.access_token_lifetime)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.access_token_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt
