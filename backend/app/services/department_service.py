from fastapi import HTTPException
from sqlalchemy import Sequence, desc

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models import Departments
from app.schemas.department_schema import *


async def get_departments(
        db: AsyncSession
) -> Sequence[Departments]:

    result = await db.execute(select(Departments).order_by(desc(Departments.dept_id)))
    return result.scalars().all()

async def get_department_by_id(
        department_id: int,
        db: AsyncSession
) -> Departments:

    result = await db.execute(select(Departments).where(Departments.dept_id == department_id))
    department = result.scalar_one_or_none()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    return department

async def create_dept(
        db: AsyncSession,
        department: DepartmentCreate
) -> Departments:

    db_departments: Departments = Departments(
        dept_name= department.dept_name,
    )
    db.add(db_departments)
    await db.commit()
    await db.refresh(db_departments)
    return db_departments

async def update_departments_by_id(
        db: AsyncSession, 
        dept_id: int,
        department_data: DepartmentUpdate 
):
    result = await db.execute(select(Departments).where(Departments.dept_id == dept_id))
    department = result.scalar_one_or_none()

    if not department:
        raise HTTPException(status_code=404, detail=f"Department: '{dept_id}' not found")
    
    for key, value in department_data.model_dump(exclude_unset=True).items():
        setattr(department, key, value)

    await db.commit()
    await db.refresh(department)
    return department
