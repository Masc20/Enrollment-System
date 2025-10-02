from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from app.db import get_db
from app.schemas.student import StudentCreate, StudentOut
from app.services.student_service import create_student, list_students, get_student_by_id

router = APIRouter()

# @router.post("/", response_model=StudentOut)
# async def add_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
#     return await create_student(db, student)

@router.get("/", response_model=list[StudentOut])
async def get_students(db: AsyncSession = Depends(get_db)):
    return await list_students(db)


@router.get("/{student_id}", response_model=StudentOut)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student