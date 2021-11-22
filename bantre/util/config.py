import os
from pydantic import BaseSettings
from functools import lru_cache


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    access_token_key: str
    refresh_token_key: str
    jwt_algorithm: str = "HS256"
    access_token_lifetime: int = 30

    class Config:
        env_file = ".env"
