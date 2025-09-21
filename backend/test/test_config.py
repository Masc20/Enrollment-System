import pytest
from backend.app.config import settings

@pytest.mark.asyncio
def test_database_url():
    """Check if DATABASE_URL is loaded from .env"""
    assert settings.DATABASE_URL is not None, "DATABASE_URL is missing in .env"
    assert settings.DATABASE_URL.startswith("postgresql+asyncpg"), \
        "DATABASE_URL must use asyncpg driver"

    print("DATABASE_URL =", settings.DATABASE_URL)