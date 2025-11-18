from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings
from app.schemas.course_schema import *
from app.services.course_service import *
from app.utils.delete_row import delete_by_id

router = APIRouter()

@router.get("/", response_model=PaginatedCourses)
async def courses(
        db: AsyncSession = Depends(get_db),
        page: int = 1,
        limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT
        )
) -> dict[str, Courses]:

    data = await get_courses(db, page=page, limit=limit)
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_courses": data["total_items"],
        "total_pages": data["total_pages"],
        "courses": data["items"],
    }

@router.get("/{course_id}", response_model=CourseOut)
async def course(
        course_id: int,
        db: AsyncSession = Depends(get_db),
) -> Courses:
    return await get_course(db, course_id)

@router.post("/new_course", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def new_course(
        new_course: CourseCreate,
        db: AsyncSession = Depends(get_db)
):

    return await create_course(db, new_course)

@router.patch("/update/{course_id}", response_model=CourseOut)
async def update_course(
    course_id: int, 
    course_data: CourseUpdate, 
    db: AsyncSession = Depends(get_db)
):
    return await update_course_by_id(db, course_id=course_id, course_data=course_data)

@router.delete("/delete/{course_id}", status_code=status.HTTP_200_OK)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await delete_by_id(db, Courses, course_id=course_id)