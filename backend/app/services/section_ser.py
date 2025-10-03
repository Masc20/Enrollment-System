from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from app.utils.pagination import paginate_query


# Model/s
from app.models.Courses import Courses
from app.models.Sections import Sections

# Schema/s
from app.schemas.section_sch import SectionCreate

async def create_section(db: AsyncSession, section: SectionCreate) -> Sections:

    if section.course_id:
        course_id = section.course_id
        # validate course exists
        result = await db.execute(select(Courses).where(Courses.course_id == course_id))
        course = result.scalar_one_or_none()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

    elif section.course_code:
        # lookup by code
        result = await db.execute(select(Courses).where(Courses.course_code == section.course_code))
        course = result.scalar_one_or_none()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        course_id = course.course_id

    else:
        raise HTTPException(status_code=400, detail="Either course_id or course_code is required")

    db_section = Sections(
        section_name=section.section_name,
        year_level=section.year_level,
        course_id=course_id
    )

    db.add(db_section)
    await db.commit()
    await db.refresh(db_section)
    return db_section

async def get_section(db: AsyncSession, section_id: int) -> Sections:
    result = await db.execute(select(Sections).where(Sections.section_id == section_id).options(selectinload(Sections.course)))
    section = result.scalar_one_or_none()
    print(section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    return section

async def get_all_section(db: AsyncSession, page: int = 1, limit: int = None) -> Sections:
    return await paginate_query(db, Sections, page=page, limit=limit, options=[selectinload(Sections.course)])
