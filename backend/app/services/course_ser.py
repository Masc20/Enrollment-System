from fastapi import HTTPException
from sqlalchemy import Sequence

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Departments

# Model/s
from app.models.Courses import Courses

# Schema/s
from app.schemas.course_sch import CourseCreate

async def get_courses(db: AsyncSession) -> Sequence[Courses]:
    result = await db.execute(select(Courses))
    return result.scalars().all()

async def get_course(db: AsyncSession, course_id: int) -> Courses:
    result = await db.execute(select(Courses).where(Courses.course_id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

async def create_course(db: AsyncSession, course: CourseCreate) -> Courses:

    if course.dept_id:
        dept_id = course.dept_id
        # validate if department exist
        result = await db.execute(select(Departments).where(Departments.dept_id == dept_id))
        department = result.scalar_one_or_none()
        if not department:
            raise HTTPException(status_code=404, detail="Department not found")

    elif course.dept_name:
        # lookup by name
        result = await db.execute(select(Departments).where(Departments.dept_name == course.dept_name))
        department = result.scalar_one_or_none()
        if not department:
            raise HTTPException(status_code=404, detail="Department not found")
        dept_id = department.dept_id

    else:
        raise HTTPException(status_code=400, detail="Either dept_id or dept_name is required")

    db_course = Courses(
        course_name= course.course_name,
        course_code= course.course_code,
        dept_id= dept_id,
    )

    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course
