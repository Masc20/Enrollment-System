from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.Student import Student
from app.schemas.Student import StudentCreate

async def create_student(db: AsyncSession, student: StudentCreate):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

async def list_students(db: AsyncSession):
    result = await db.execute(select(Student))
    return result.scalars().all()
