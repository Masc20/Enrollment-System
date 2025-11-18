from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.EnrollmentDetails import EnrollmentDetails
from app.schemas.enrollment_details_schema import *

async def create_enrollment_detail(
    db: AsyncSession,
    data: EnrollmentDetailCreate
) -> EnrollmentDetails:

    db_detail = EnrollmentDetails(
        enrollment_id=data.enrollment_id,
        schedule_id=data.schedule_id
    )

    db.add(db_detail)
    await db.commit()
    await db.refresh(db_detail)

    return db_detail

async def get_enrollment_detail(
    db: AsyncSession,
    detail_id: int
) -> EnrollmentDetails:

    result = await db.execute(
        select(EnrollmentDetails).where(
            EnrollmentDetails.enroll_detail_id == detail_id
        )
    )
    detail = result.scalar_one_or_none()

    if not detail:
        raise HTTPException(status_code=404, detail="Enrollment detail not found")

    return detail

async def update_enrollment_detail_partial(
    db: AsyncSession,
    detail_id: int,
    data: EnrollmentDetailUpdate
) -> EnrollmentDetails:

    detail = await get_enrollment_detail(db, detail_id)

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(detail, key, value)

    await db.commit()
    await db.refresh(detail)

    return detail
