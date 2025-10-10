from fastapi import HTTPException
from sqlalchemy import Sequence, Select
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Enrollments, Courses, Sections, Students
from app.utils.pagination import paginate_query


async def create_enrollment(
    db: AsyncSession,
    new_enrollment: Enrollments
) -> Enrollments:

    if new_enrollment.course_id:
        result = await db.execute(select(Courses).where(Courses.course_id == new_enrollment.course_id))
        course = result.scalar_one_or_none()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        course_id = new_enrollment.course_id

    if new_enrollment.section_id:
        result = await db.execute(select(Sections).where(Sections.section_id == new_enrollment.section_id))
        section = result.scalar_one_or_none()
        if not section:
            raise HTTPException(status_code=404, detail="Section not found")

        section_id = new_enrollment.section_id

    if new_enrollment.student_id:
        result = await db.execute(select(Students).where(Students.student_id == new_enrollment.student_id))
        student = result.scalar_one_or_none()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        student_id = new_enrollment.student_id

    db_enrollment = Enrollments(
        academic_year= new_enrollment.academic_year,
        semester= new_enrollment.semester,
        year_level= new_enrollment.year_level,
        student_id= student_id,
        section_id= section_id,
        course_id= course_id
    )

    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    return db_enrollment

async def list_enrollments(
        db: AsyncSession,
        page: int = 1,
        limit: int = None,
):
    return await paginate_query(
        db,
        Enrollments,
        page=page,
        limit=limit,
        options=[
            selectinload(Enrollments.course),
            selectinload(Enrollments.section),
            selectinload(Enrollments.student),
        ]
    )