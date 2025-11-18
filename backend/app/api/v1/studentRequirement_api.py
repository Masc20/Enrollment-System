from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings
from app.schemas.requirement_schema import *
from app.services.studentRequirement_services import *
from app.utils.delete_row import delete_by_id

router = APIRouter()

@router.get("/{stud_req_id}", response_model=StudentRequirementOut, description="Filtered by Student ID")
async def get_requirement(
    stud_req_id: int,
    db: AsyncSession = Depends(get_db)
):
    req = await list_student_requirements_by_student(db, stud_req_id)
    if not req:
        raise HTTPException(status_code=404, detail="Requirement not found")
    return req

@router.get("/", summary="List all student requirements (paginated)")
async def list_all_requirements(
    page: int = Query(1, ge=1),
    limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT
        ),
    db: AsyncSession = Depends(get_db)
):
    return await list_student_requirements(db, page, limit)

@router.post("/", response_model=StudentRequirementOut)
async def create_student_requirement(
    data: StudentRequirementCreate,
    db: AsyncSession = Depends(get_db)
):
    return await add_students_requirements(db, data)

@router.put("update/{stud_req_id}", response_model=StudentRequirementOut)
async def update_student_requirement(
    stud_req_id: int,
    update_data: StudentRequirementUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await update_status(db, stud_req_id, update_data)

@router.delete("/delete/{stud_req_id}", status_code=status.HTTP_200_OK)
async def delete_student_requirement(
    stud_req_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await delete_by_id(db, StudentRequirements, stud_req_id)