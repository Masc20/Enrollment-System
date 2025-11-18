from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings
from app.schemas.teacher_schema import *
from app.services.teacher_service import *
from app.utils.delete_row import delete_by_id
from app.utils.pagination import paginate_query

router = APIRouter()

@router.get("/", response_model=PaginatedTeacherOut)
async def teachers(
    db: AsyncSession = Depends(get_db),
    page: int = 1,
    limit: int = Query(
        default=settings.DEFAULT_PAGE_LIMIT,
        le=settings.MAX_PAGE_LIMIT
    )
):
    data = await paginate_query(db, Teachers, page=page, limit=limit)
    
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_teachers": data["total_items"],
        "total_pages": data["total_pages"],
        "teachers": data["items"],
    }

@router.get("/{teacher_id}", response_model=TeacherOut)
async def get_teacher(teacher_id: int, db: AsyncSession = Depends(get_db)):
    return await get_teacher_by_id(db, teacher_id=teacher_id)

@router.patch("/update/{teacher_id}", response_model=TeacherOut)
async def udpate_teacher(
    teacher_id: int, 
    teacher_data: TeacherUpdate, 
    db: AsyncSession =Depends(get_db)
):
    return await update_teacher_partial(db, teacher_id=teacher_id, data=teacher_data)

@router.delete("/delete/{teacher_id}", status_code=status.HTTP_200_OK)
async def delete_teacher(
    teacher_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await delete_by_id(db, Teachers, teacher_id)