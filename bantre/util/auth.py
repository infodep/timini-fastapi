from functools import wraps
import jwt

from bantre import app
from bantre.system.user import UserModel, User

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)



def decode_token(token: str) -> User:


    return User(
        uid=1,  
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
