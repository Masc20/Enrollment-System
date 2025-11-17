from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.Administrators import Administrators
from app.schemas.administrator_schema import *

from app.utils.security import get_password_hash

async def add_new_admin(db: AsyncSession, new_admin: AdministratorCreate):
    result = await db.execute(select(Administrators).where(Administrators.username == new_admin.username))
    isExists = result.scalar_one_or_none

    if not isExists:
        raise HTTPException(status_code=400, detail=f"{new_admin.username} is already taken")
    
    hashed_password = get_password_hash(new_admin.password)
    
    db_new_admin = Administrators (
        username=new_admin.username,
        password=hashed_password,
        role=new_admin.role,
    )
    db.add(db_new_admin)
    await db.commit()
    await db.refresh(db_new_admin)
    return {"detail": "admin added successfully"}

async def update_admin(db: AsyncSession, admin_id: int, updated_admin: AdministratorUpdate):
    result = await db.execute(select(Administrators).where(Administrators.admin_id == updated_admin.admin_id))
    isExists = result.scalar_one_or_none

    if not isExists:
        raise HTTPException(status_code=400, detail=f"admin_id: '{admin_id}' not found")