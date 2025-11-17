import pytest
from app.config import settings

@pytest.mark.asyncio
async def test_database_ASYNC_url():
    """Check if DATABASE_URL is loaded from .env"""
    assert settings.DATABASE_URL_ASYNC is not None, "DATABASE_URL is missing in .env"
    assert settings.DATABASE_URL_ASYNC.startswith("postgresql+asyncpg"), \
        "DATABASE_URL must use asyncpg driver"

@pytest.mark.asyncio
async def test_database_SYNC_url():
    """Check if DATABASE_URL is loaded from .env"""
    assert settings.DATABASE_URL_SYNC is not None, "DATABASE_URL is missing in .env"
    assert settings.DATABASE_URL_SYNC.startswith("postgresql+psycopg2"), \
        "DATABASE_URL must use psycopg2 driver"