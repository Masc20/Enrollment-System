from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.administrator_service import *
from app.db import get_db
from app.config import settings

router = APIRouter()

@router.get("/", response_model=PaginatedAdminOut)
async def get_admins(
    db: AsyncSession = Depends(get_db),
    page: int = 1,
    limit: int = Query(
        default=settings.DEFAULT_PAGE_LIMIT,
        le=settings.MAX_PAGE_LIMIT
    )
):
    data = list_of_admins(db, page=page, limit=limit)

    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_admins": data["total_items"],
        "total_pages": data["total_pages"],
        "admins": data["items"],
    }

@router.get("/{admin_id}", response_model=AdministratorOut)
async def get_admin( admin_id: int, db: AsyncSession = Depends(get_db)):
    return await get_admin_by_id(db, admin_id=admin_id)

@router.post("/new_admin", response_model=AdministratorOut)
async def add_admin(new_admin: AdministratorCreate, db: AsyncSession = Depends(get_db)):
    return await add_new_admin(db, new_admin=new_admin)

@router.patch("/update/{update_id}", response_model=AdministratorOut)
async def update_admin(admin_id: int, new_data: AdministratorUpdate, db: AsyncSession = Depends(get_db)):
    return await update_admin_by_id(db, admin_id=admin_id, updated_admin=new_data)

@router.delete("delete/{admin_id}", status_code=status.HTTP_200_OK)
async def delete_admin(admin_id: int, db: AsyncSession):
    return await delete_admin_by_id(db, admin_id=admin_id )