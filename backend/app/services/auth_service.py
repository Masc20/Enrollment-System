from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

from app.models.Administrators import Administrators
from app.utils.security import verify_password

async def authenticate_admin(db: AsyncSession, username: str, password: str) -> Administrators:
    result = await db.execute(select(Administrators).where(Administrators.username == username))
    admin = result.scalar_one_or_none()
    
    if not admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed")
    
    if not verify_password(password, admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed")
    
    return admin