from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings


from app.schemas.course_schema import *

from app.services.course_service import *

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
    print("Debug: hello api")
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_courses": data["total_items"],
        "total_pages": data["total_pages"],
        "courses": data["items"],
    }

@router.get("/{student_id}", response_model=CourseOut)
async def course(
        student_id: int,
        db: AsyncSession = Depends(get_db),
) -> Courses:
    return await get_course(db, student_id)

@router.post("/new_course", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def new_course(
        new_course: CourseCreate,
        db: AsyncSession = Depends(get_db)
):

    return await create_course(db, new_course)

