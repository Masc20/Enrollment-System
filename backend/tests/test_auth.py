import pytest
from httpx import AsyncClient

BASE_URL = "http://127.0.0.1:8000"  #running FastAPI server

# -------------------------------
# Test login success
# -------------------------------
@pytest.mark.asyncio
async def test_login_success():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/auth/login", json={
            "username": "success@test.com",
            "password": "mypassword"  # plain password used for login
        })
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["message"] == "Login successful"

# -------------------------------
# Test login failure (wrong password)
# -------------------------------
@pytest.mark.asyncio
async def test_login_failure_wrong_password():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/auth/login", json={
            "username": "success@test.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        assert response.json()["detail"] == "Login failed"

# -------------------------------
# Test login failure (user not found)
# -------------------------------
@pytest.mark.asyncio
async def test_login_failure_user_not_found():
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/auth/login", json={
            "username": "nouser@test.com",
            "password": "any"
        })
        assert response.status_code == 401
        assert response.json()["detail"] == "Login failed"
