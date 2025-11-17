from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import authenticate_admin
from app.db import get_db

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    admin = await authenticate_admin(db, data.username, data.password)
    
    return LoginResponse(
        username=admin.username,
        role=admin.role,
        message="Login successful"
    )