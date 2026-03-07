# app/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str

    DATABASE_URL: str

    SECRET_KEY: str
    PAYSTACK_SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()
