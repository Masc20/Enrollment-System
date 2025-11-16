from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

from app.schemas.requirement_schema import *

from app.services.requirement_sevice import *

router = APIRouter()

@router.get("/", response_model = RequirementOut)
async def get_requirements(db: AsyncSession = Depends(get_db)):
    return await get_all_requiments(db)


@router.post("/new_requirements", response_model = RequirementCreate, status_code=status.HTTP_201_CREATED)
async def add_requirements(
    new_requirements: RequirementCreate, 
    db: AsyncSession
    ) -> Requirements:
    
    return await add_new_requirements(db, new_requirements)

@router.put("update_requirement", response_model=RequirementUpdate)
async def change_requirement(
    requirement: RequirementUpdate,
    db: AsyncSession
) -> Requirements: 

    return await update_requirement(db, requirement)