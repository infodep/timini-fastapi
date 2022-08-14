from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import BaseModel

from bantre.modules.auth.auth_model import TokenModel
from bantre.util.auth import authenticate_user, create_access_token, decode_token
from bantre.util import config
from bantre.database import Base, get_db

auth_router = APIRouter()

# Return model
class Token(BaseModel):
    id: int
    exp: datetime
    token_type: str


@auth_router.post("/login", response_model=Token)
async def login(
    formdata: OAuth2PasswordRequestForm = Depends(),
    settings: config.Settings = Depends(config.get_settings),
):
    user = authenticate_user(get_db(), formdata.username, formdata.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_lifetime)
    access_token = create_access_token(id=user.id, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


class Tokens(BaseModel):
    access_token: Token
    refresh_token: Token


@auth_router.post("/refresh", response_model=Tokens)
async def refresh(access_token: str):
    user = decode_token(get_db(), access_token)
