import pytest
import httpx
from app.main import app

@pytest.mark.asyncio
async def test_db_connection():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/test-db")
    assert response.status_code == 200
    assert response.json()["status"].startswith("✅")
