from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.pagination import paginate_query

# Model/s
from app.models import Courses
from app.models import Departments


# Schema/s
from app.schemas.course_schema import *

async def get_courses(
        db: AsyncSession,
        page: int = 1,
        limit: int = None,
):
    
    return await paginate_query(
        db,
        Courses,
        page=page,
        limit=limit,
        options=[
            selectinload(Courses.department)
        ],
    )

async def get_course(
        db: AsyncSession,
        course_id: int
) -> Courses:

    result = await db.execute(select(Courses).where(Courses.course_id == course_id).options(selectinload(Courses.department)))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

async def create_course(
        db: AsyncSession,
        course: CourseCreate
) -> Courses:

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
        course_name = course.course_name,
        course_code = course.course_code,
        dept_id = dept_id,
    )

    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


async def update_course_by_id(
        db: AsyncSession, 
        course_id: int, 
        course_data: CourseUpdate
):
    result = await db.execute(select(Courses).where(Courses.student_id == course_id))
    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)
    return course
