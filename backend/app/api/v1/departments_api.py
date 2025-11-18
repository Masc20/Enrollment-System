from fastapi import APIRouter, Depends, status

from app.db import get_db
from app.schemas.department_schema import *
from app.services.department_service import *
from app.utils.delete_row import delete_by_id

router = APIRouter()

@router.get("/", response_model=list[DepartmentOut])
async def departments(
    db: AsyncSession = Depends(get_db)
):
    return await get_departments(db)

@router.get("/{department_id}", response_model=DepartmentOut)
async def get_department(
    department_id: int, 
    db: AsyncSession = Depends(get_db)
):
    return await get_department_by_id(department_id=department_id, db=db)

@router.post("/new_department", response_model=DepartmentOut, status_code=status.HTTP_201_CREATED)
async def new_department(
    department: DepartmentCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_dept(db, department)

@router.patch("/update/{department_id}", response_model=DepartmentOut)
async def update_department(
    department_id: int,
    department_data: DepartmentUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await update_departments_by_id(db, department_id, department_data=department_data)

@router.delete("/delete/{department_id}", status_code=status.HTTP_200_OK)
async def delete_department(
    department_id: int,
    db: AsyncSession = Depends(get_db)  
):
    return await delete_by_id(db, Departments, department_id)