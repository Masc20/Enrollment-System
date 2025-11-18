from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings
from app.schemas.enrollment_details_schema import *
from app.services.enrollment_detail_service import *
from app.utils.delete_row import delete_by_id
from app.utils.pagination import paginate_query

router = APIRouter()

@router.get("/", response_model=PaginatedEnrollmentDetail)
async def get_all_enrollment_details(
    page: int = Query(1, ge=1),
    limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT
        ),
    db: AsyncSession = Depends(get_db)
):
    data = await paginate_query(
        db,
        EnrollmentDetails,
        page=page,
        limit=limit
    )

    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_details": data["total_items"],
        "total_pages": data["total_pages"],
        "details": data["items"],
    }

@router.get("/{detail_id}", response_model=EnrollmentDetailOut)
async def enrollment_detail(
    detail_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await get_enrollment_detail(db, detail_id)

@router.patch("/update/{detail_id}", response_model=EnrollmentDetailOut)
async def update_detail(
    detail_id: int,
    detail_data: EnrollmentDetailUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await update_enrollment_detail_partial(db, detail_id, detail_data)

@router.delete("/delete/{detail_id}", status_code=status.HTTP_200_OK)
async def delete_detail(
    detail_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await delete_by_id(db, EnrollmentDetails, detail_id)