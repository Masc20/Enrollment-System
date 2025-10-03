from fastapi import APIRouter, Depends, status, Query

from app.db import get_db

# Schema/s
from app.schemas.department_sch import *

# Service/s
from app.services.department_ser import *

router = APIRouter()

@router.get("/", response_model=list[DepartmentOut])
async def departments(db: AsyncSession = Depends(get_db)):
    return await get_departments(db)

@router.post("/new_department", response_model=DepartmentOut, status_code=status.HTTP_201_CREATED)
async def new_department(department: DepartmentCreate, db: AsyncSession = Depends(get_db)):
    return await create_dept(db, department)