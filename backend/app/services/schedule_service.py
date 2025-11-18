from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.models.Schedules import Schedules
from app.schemas.schedule_schema import *

async def create_schedule(db: AsyncSession, data: ScheduleCreate):
    new_schedule = Schedules(**data.model_dump())
    db.add(new_schedule)
    await db.commit()
    await db.refresh(new_schedule)
    return new_schedule

async def get_schedule(db: AsyncSession, schedule_id: int):
    result = await db.execute(
        select(Schedules).where(Schedules.schedule_id == schedule_id)
    )
    schedule = result.scalars().first()

    if not schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schedule not found",
        )

    return schedule