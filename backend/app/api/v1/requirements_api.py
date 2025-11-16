from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

from app.schemas.requirement_schema import *

from app.services.requirement_sevice import *

router = APIRouter()

@router.get("/", response_model =  list[RequirementOut])
async def get_requirements(db: AsyncSession = Depends(get_db)):
    return await get_all_requiments(db)


@router.post("/new_requirements", response_model = RequirementOut)
async def add_requirements(
    new_requirements: RequirementCreate, 
    db: AsyncSession = Depends(get_db)
):
    
    return await add_new_requirements(db, new_requirements)

@router.put("update_requirement/{requirement_id}", response_model=RequirementUpdate)
async def change_requirement(
    requirement_id: int,
    requirement: RequirementUpdate,
    db: AsyncSession = Depends(get_db)
): 

    return await update_requirement(db, requirement_id, requirement)