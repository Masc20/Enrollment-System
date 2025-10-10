from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

# Schema/s
from app.schemas.student_schema import *

# Service/s
from app.services.student_service import *

router = APIRouter()

# Delete
@router.delete("/delete/{student_id}", status_code=status.HTTP_200_OK)
async def remove_student(
        student_id: int,
        db: AsyncSession = Depends(get_db)
):

    return await delete_student(db, student_id)

# Patch
@router.patch("/update/{student_id}", response_model=StudentOut)
async def update_student_patch(
        student_id: int,
        student: StudentUpdate,
        db: AsyncSession = Depends(get_db)
):

    return await update_student_partial(db, student_id, student)


# Post
@router.post("/new_student", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
async def add_student(
        student: StudentCreate,
        db: AsyncSession = Depends(get_db)
):

    return await create_student(db, student)



# Get
@router.get("/", response_model= PaginatedStudents)
async def get_students(
        db: AsyncSession = Depends(get_db),
        page: int = 1,
        limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT
        )
) -> dict[str, Students]:

    data = await list_students(db, page=page, limit=limit)
    # Rename items -> students for schema
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_students": data["total_items"],
        "total_pages": data["total_pages"],
        "students": data["items"],
    }

@router.get("/{student_id}", response_model=StudentOut)
async def get_student(
        student_id: int,
        db: AsyncSession = Depends(get_db)
) -> Students:
    return await get_student_by_id(db, student_id)