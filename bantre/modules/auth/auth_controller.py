from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from bantre.modules.article.article_model import AuthModel
from bantre.system.user import UserModel, UserInDB

auth_router = APIRouter()

@auth_router.post("/login")
async def login(formdata: OAuth2PasswordRequestForm = Depends()):
    query = select(UserModel).where(UserModel.username == formdata.username)
    user_dict = Session.execute(query).fetchone()
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB