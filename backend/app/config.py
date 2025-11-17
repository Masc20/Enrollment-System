from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar

class Settings(BaseSettings):
    DATABASE_URL_ASYNC: str
    DATABASE_URL_SYNC: str
    # SECRET_KEY: str
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DEFAULT_PAGE_LIMIT: ClassVar[int]  = 20
    MAX_PAGE_LIMIT: ClassVar[int] = 100  # optional, to prevent huge queries

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
