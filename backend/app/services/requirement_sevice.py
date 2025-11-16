from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Sequence

from app.models.Requirements import Requirements

from app.schemas.requirement_schema import *


async def get_all_requiments (db: AsyncSession) -> Sequence[Requirements]:
    result = await db.execute(select(Requirements))
    requirements = result.scalars().all()
    if not requirements:
        raise HTTPException(status_code=404, detail="No Requirement/s set")
    return requirements


async def get_requirement (db: AsyncSession, requirement_id: int):
    result = await db.execute(select(Requirements).where(Requirements.req_id == requirement_id))
    requirement = result.scalar_one_or_none
    if not requirement:
        raise HTTPException(status_code=404, detail="Requirement Not found")
    return requirement

async def add_new_requirements(
        db: AsyncSession,
        new_requirements: RequirementCreate
        ) -> Requirements:
    result = await db.execute(
        select(Requirements)
        .where(Requirements.req_name == new_requirements.req_name))
    
    isRequirementExists = result.scalar_one_or_none()
    
    # check if it already exists
    if isRequirementExists:
        raise HTTPException(status_code=422, detail="Requirement already exists")
    
    db_requirement = Requirements(
        req_name = new_requirements.req_name
    )

    db.add(db_requirement)
    await db.commit()
    await db.refresh(db_requirement)
    return db_requirement

async def update_requirement(
        db: AsyncSession,
        update_requirements: RequirementUpdate
        ) -> Requirements:

    result = await db.execute(
        select(Requirements)
        .where(Requirements.req_name == update_requirements.req_name))
    
    db_requirements = result.scalar_one_or_none()

    # Check if Requirement Exists
    if not db_requirements:
        raise HTTPException(
            status_code=404, 
            detail=f"{update_requirements.req_name} not found"
            )
    
    # For new columns added, if ever there is
    for key, value in update_requirements.model_dump(exclude_unset=True).items():
        setattr(db_requirements, key, value)


    db.add(db_requirements)
    await db.commit()
    await db.refresh(db_requirements)
    return db_requirements 