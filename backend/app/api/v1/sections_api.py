from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

# Schema/s
from app.schemas.section_sch import *

# Services
from app.services.section_ser import *

router = APIRouter()


@router.post("/new_section", response_model=SectionCreate, status_code=status.HTTP_201_CREATED)
async def new_section(sections: SectionCreate, db: AsyncSession = Depends(get_db)):
    return await create_section(db, sections)

@router.get("/section/{section_id}", response_model=SectionOut)
async def section(section_id: int, db: AsyncSession = Depends(get_db)):
    return await get_section(db, section_id)

@router.get("/", response_model=PaginatedSections)
async def get_sections(db: AsyncSession = Depends(get_db),  page: int = 1, limit: int = Query(default=None, le=settings.MAX_PAGE_LIMIT)):
    data = await get_all_section(db, page=page, limit=limit)
    # Rename items -> section for schema
    return {
        "page": data["page"],
        "limit": data["limit"],
        "total_sections": data["total_items"],
        "total_pages": data["total_pages"],
        "sections": data["items"],
    }

