import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the application."""

    # JWT settings
    secret_key: str = os.getenv("SECRET_KEY", "secret-key")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


settings = Settings()
