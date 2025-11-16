from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

# Schema/s
from app.schemas.enrollment_schema import *

# Services
from app.services.enrollment_service import *

router = APIRouter()

@router.post("/new_enrollee", response_model=EnrollmentOut, status_code=status.HTTP_201_CREATED)
async def new_enrollment(
        new_enrollee: EnrollmentCreate,
        db: AsyncSession = Depends(get_db),
):
    return await create_enrollment(db, new_enrollee)

@router.get("/", response_model=EnrollmentPaginated, status_code=status.HTTP_200_OK)
async def enrollments(
        db: AsyncSession = Depends(get_db),
        page: int = 1,
        limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT
        )
):
    data = await list_enrollments(
        db,
        page=page,
        limit=limit,
    )

    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_enrollments": data["total_items"],
        "total_pages": data["total_pages"],
        "enrollments": data["items"],
    }

@router.put("/{enrollment_id}", response_model=EnrollmentOut)
async def update_enrollment_route(
    enrollment_id: int,
    update_data: EnrollmentUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await update_enrollment(db, enrollment_id, update_data)
