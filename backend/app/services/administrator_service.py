from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.Administrators import Administrators
from app.schemas.administrator_schema import *
from app.utils.pagination import paginate_query
from app.utils.security import get_password_hash

async def list_of_admins(
        db: AsyncSession, 
        page: int = 1, 
        limit: int = None
):
    return await paginate_query(
        db=db,
        model=AdministratorOut,
        page=page,
        limit=limit,
    )

async def get_admin_by_id(
        db: AsyncSession,
        admin_id: int
):
    result = await db.execute(select(Administrators).where(Administrators.admin_id == admin_id))
    admin = result.scalar_one_or_none()

    if not admin:
        raise HTTPException(status_code=404, detail=f"admin: '{admin_id}' not found")
    
    return admin

async def add_new_admin(db: AsyncSession, new_admin: AdministratorCreate):
    result = await db.execute(select(Administrators).where(Administrators.username == new_admin.username))
    isExists = result.scalar_one_or_none()

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

async def update_admin_by_id(db: AsyncSession, admin_id: int, updated_admin: AdministratorUpdate):
    result = await db.execute(select(Administrators).where(Administrators.admin_id == updated_admin.admin_id))
    db_admin = result.scalar_one_or_none()

    if not db_admin:
        raise HTTPException(status_code=404, detail=f"admin_id: '{admin_id}' not found")
    
    for key, value in db_admin.model_dump(exclude_unset=True).items():
        setattr(db_admin, key, value)
    
    await db.commit()
    await db.refresh(db_admin)
    return db_admin
    
async def delete_admin_by_id(db: AsyncSession, admin_id: int):
    result = await db.execute(select(Administrators).where(Administrators.admin_id == admin_id))
    db_admin = result.scalar_one_or_none()

    if not db_admin:
        raise HTTPException(status_code=404, detail=f"admin_id: '{admin_id}' not found" )

    await db.delete(db_admin)
    await db.commit()
    return {"detail": "Deleted Successfully"}