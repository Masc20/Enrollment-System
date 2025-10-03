from fastapi import APIRouter, Depends, status

from app.db import get_db


from app.schemas.course_sch import *

from app.services.course_ser import *

router = APIRouter()

@router.get("/", response_model=CourseOut)
async def courses(db: AsyncSession = Depends(get_db)):
    return await get_courses(db)

@router.post("/new_course", status_code=201)
async def new_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    return await create_course(db, course)

