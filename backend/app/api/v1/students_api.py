from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.schemas.student import StudentCreate, StudentOut, StudentUpdate
from app.services.student_service import *

router = APIRouter()

@router.delete("/delete/{student_id}", status_code=200)
async def remove_student(student_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_student(db, student_id)

@router.patch("/update/{student_id}", response_model=StudentOut)
async def update_student_patch(student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_db)):
    return await update_student_partial(db, student_id, student)

@router.post("/new_student", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
async def add_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    return await create_student(db, student)

@router.get("/", response_model=list[StudentOut])
async def get_students(db: AsyncSession = Depends(get_db)):
    return await list_students(db)

@router.get("/{student_id}", response_model=StudentOut)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student