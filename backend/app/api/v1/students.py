from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas.Student import StudentCreate, StudentOut
from app.services.student_service import create_student, list_students

router = APIRouter()

@router.post("/", response_model=StudentOut)
async def add_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    return await create_student(db, student)

@router.get("/", response_model=list[StudentOut])
async def get_students(db: AsyncSession = Depends(get_db)):
    return await list_students(db)
