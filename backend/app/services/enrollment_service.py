from fastapi import HTTPException
from sqlalchemy import Sequence, Select
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Enrollments, Courses, Sections, Students
from app.schemas.enrollment_schema import *
from app.utils.pagination import paginate_query


async def create_enrollment(
    db: AsyncSession,
    new_enrollment: EnrollmentCreate
):

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

async def get_enrollment_by_id(
    db: AsyncSession,
    enrollment_id: int
):
    result = await db.execute(select(Enrollments).where(Enrollments.enrollment_id == enrollment_id))
    enrollment = result.scalar_one_or_none()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollee not found")
    
    return enrollment

async def update_enrollment_by_id(
    db: AsyncSession,
    enrollment_id: int,
    update_data: EnrollmentUpdate
):

    # --------------------------------------------------
    # 1️⃣ Fetch existing enrollment
    # --------------------------------------------------
    result = await db.execute(
        select(Enrollments).where(Enrollments.enrollment_id == enrollment_id)
    )
    db_enrollment = result.scalar_one_or_none()

    if not db_enrollment:
        raise HTTPException(
            status_code=404,
            detail=f"Enrollment with ID {enrollment_id} not found"
        )

    # --------------------------------------------------
    # 2️⃣ Extract update fields
    # --------------------------------------------------
    update_fields = update_data.model_dump(exclude_unset=True)

    # --------------------------------------------------
    # 3️⃣ Validate foreign keys if included
    # --------------------------------------------------
    if "student_id" in update_fields:
        r = await db.execute(select(Students).where(
            Students.student_id == update_fields["student_id"]
        ))
        if not r.scalar_one_or_none():
            raise HTTPException(status_code=404, detail="Student not found")

        db_enrollment.student_id = update_fields["student_id"]

    if "section_id" in update_fields:
        r = await db.execute(select(Sections).where(
            Sections.section_id == update_fields["section_id"]
        ))
        if not r.scalar_one_or_none():
            raise HTTPException(status_code=404, detail="Section not found")
        
        db_enrollment.section_id = update_fields["section_id"]

    if "course_id" in update_fields:
        r = await db.execute(select(Courses).where(
            Courses.course_id == update_fields["course_id"]
        ))
        if not r.scalar_one_or_none():
            raise HTTPException(status_code=404, detail="Course not found")
        
        db_enrollment.course_id = update_fields["course_id"]

    # --------------------------------------------------
    # 4️⃣ Update normal fields (academic_year, semester, year_level)
    # --------------------------------------------------
    for key, value in update_fields.items():
        if key not in {"student_id", "section_id", "course_id"}:
            setattr(db_enrollment, key, value)

    # --------------------------------------------------
    # 5️⃣ Save changes
    # --------------------------------------------------
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)

    return db_enrollment
