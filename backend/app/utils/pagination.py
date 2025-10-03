from math import ceil
from typing import Any
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import settings

async def paginate_query(db: AsyncSession, model, page: int = 1, limit: int = None, options: list[Any] = None):
    """
    Generic pagination helper for any SQLAlchemy model.
    Returns dict with pagination metadata and items.
    """
    limit = limit or settings.MAX_PAGE_LIMIT
    offset = (page - 1) * limit

    stmt = select(model).offset(offset).limit(limit)
    if options:
        for opt in options:
            stmt = stmt.options(opt)


    # Fetch items
    result = await db.execute(stmt)
    items = result.scalars().all()

    # Count total
    total_result = await db.execute(select(func.count()).select_from(model))
    total = total_result.scalar() or 0

    total_pages = ceil(total / limit)

    return {
        "page": page,
        "limit": limit,
        "total_items": total,
        "total_pages": total_pages,
        "items": items
    }
