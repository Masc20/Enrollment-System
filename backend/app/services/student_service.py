from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import HTTPException

from app.models.Students import Students
from app.schemas.student import StudentCreate, StudentUpdate

async def create_student(db: AsyncSession, student: StudentCreate):
    db_student = Students(
        student_number=student.student_number,
        middle_name=student.middle_name,
        first_name=student.first_name,
        last_name=student.last_name,
        birth_date=student.birth_date,
        gender=student.gender,
        email=student.email,
        contact_number=student.contact_number,
        address=student.address,
        admission_status=student.admission_status,
        enrollment_status=student.enrollment_status,

    )
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

async def update_student_partial(db: AsyncSession, student_id: int, student: StudentUpdate):
    result = await db.execute(select(Students).where(Students.student_id == student_id))
    db_student = result.scalar_one_or_none()

    # check if_student_exist
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update ONLY fields provided in request
    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(db_student, key, value)

    await db.commit()
    await db.refresh(db_student)
    return db_student

async def delete_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Students).where(Students.student_id == student_id))
    db_student = result.scalar_one_or_none()

    # check if_student_exist
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    await db.delete(db_student)
    await db.commit()
    return {"detail": f"Student with id {student_id} deleted successfully"}

async def list_students(db: AsyncSession):
    result = await db.execute(select(Students))
    return result.scalars().all()

async def get_student_by_id(db: AsyncSession, student_id: int):
    result = await db.execute(select(Students).where(Students.student_id == student_id))
    return result.scalar_one_or_none()  # ✅ returns single object or None
