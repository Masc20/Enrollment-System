from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import HTTPException

from app.models.Teachers import *
from app.utils.pagination import paginate_query
from app.schemas.teacher_schema import *

async def create_teacher(
    db: AsyncSession,
    data: TeacherCreate
) -> Teachers:

    db_teacher = Teachers(
        firstname=data.firstname,
        lastname=data.lastname,
        contact_number=data.contact_number,
        email=data.email
    )

    db.add(db_teacher)
    await db.commit()
    await db.refresh(db_teacher)

    return db_teacher

async def get_teacher_by_id(
    db: AsyncSession,
    teacher_id: int
) -> Teachers:

    result = await db.execute(
        select(Teachers).where(Teachers.teacher_id == teacher_id)
    )
    teacher = result.scalar_one_or_none()

    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return teacher

async def update_teacher_partial(
    db: AsyncSession,
    teacher_id: int,
    data: TeacherUpdate
) -> Teachers:

    teacher = await get_teacher_by_id(db, teacher_id)

    # update only provided fields
    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(teacher, key, value)

    await db.commit()
    await db.refresh(teacher)

    return teacher