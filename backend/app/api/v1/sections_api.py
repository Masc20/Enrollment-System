from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings
from app.schemas.section_schema import *
from app.services.section_service import *
from app.utils.delete_row import delete_by_id

router = APIRouter()

@router.get("/section/{section_id}", response_model=SectionOut)
async def section(
        section_id: int,
        db: AsyncSession = Depends(get_db)
):

    return await get_section(db, section_id)

@router.get("/", response_model=PaginatedSections)
async def get_sections(
        db: AsyncSession = Depends(get_db),
        page: int = 1,
        limit: int = Query(
            default=settings.DEFAULT_PAGE_LIMIT,
            le=settings.MAX_PAGE_LIMIT)
) -> dict[str, Sections]:

    data = await get_all_section(db, page=page, limit=limit)
    # Rename items -> section for schema
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_sections": data["total_items"],
        "total_pages": data["total_pages"],
        "sections": data["items"],
    }

@router.post("/new_section", response_model=SectionCreate, status_code=status.HTTP_201_CREATED)
async def new_section(
    sections: SectionCreate,
    db: AsyncSession = Depends(get_db)
):

    return await create_section(db, sections)

@router.patch("/update/{section_id}", response_model=SectionOut)
async def update_section(
    section_id: int, 
    section_data: SectionUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await update_section_by_id(db, section_id=section_id, section_data=section_data)

@router.delete("/delete/{section_id}", status_code=status.HTTP_200_OK)
async def delete_section(
    section_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await delete_by_id(db, Sections, section_id)