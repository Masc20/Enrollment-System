from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.Students import Students
from app.schemas.student import StudentCreate

async def create_student(db: AsyncSession, student: StudentCreate):
    db_student = Students(name=student.name, email=student.email)
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

async def list_students(db: AsyncSession):
    result = await db.execute(select(Students))
    return result.scalars().all()

async def get_student_by_id(db: AsyncSession, student_id: int):
    result = await db.execute(select(Students).where(Students.student_id == student_id))
    return result.scalar_one_or_none()  # ✅ returns single object or None
