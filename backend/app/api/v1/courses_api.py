from fastapi import APIRouter, Depends, status

from app.db import get_db


from app.schemas.course_schema import *

from app.services.course_service import *

router = APIRouter()

@router.get("/", response_model=list[CourseOut])
async def courses(
        db: AsyncSession = Depends(get_db)
) -> dict[str, Courses]:

    return await get_courses(db)

@router.get("/{student_id}", response_model=CourseOut)
async def course(
        student_id: int,
        db: AsyncSession = Depends(get_db),
) -> Courses:
    return await get_course(db, student_id)

@router.post("/new_course", status_code=201)
async def new_course(
        new_course: CourseCreate,
        db: AsyncSession = Depends(get_db)
):

    return await create_course(db, new_course)

