from math import ceil
from typing import Any
from sqlalchemy import select, func, inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.config import settings


def build_recursive_load(model, depth=1, max_depth=2):
    """
    Recursively builds selectinload() options for nested relationships.
    """
    if depth > max_depth:
        return []

    mapper = inspect(model)
    load_options = []
    for rel in mapper.relationships:
        attr = getattr(model, rel.key)
        opt = selectinload(attr)
        # Recurse into related model
        nested_opts = build_recursive_load(rel.mapper.class_, depth + 1, max_depth)
        for nopt in nested_opts:
            opt = opt.options(nopt)
        load_options.append(opt)
    return load_options


async def paginate_query(
        db: AsyncSession,
        model,
        page: int = 1,
        limit: int = None,
        options: list[Any] = None,
        auto_load_relationships: bool = True,
        max_depth: int = 2
) -> dict[str, Any]:
    """
    Generic pagination helper for any SQLAlchemy model.
    Automatically loads nested relationships up to `max_depth` levels deep.
    """
    limit = limit or settings.DEFAULT_PAGE_LIMIT
    offset = (page - 1) * limit
    print("Debug: hello pagination")
    stmt = select(model).offset(offset).limit(limit)

    # 🔄 Automatically include relationships recursively
    if auto_load_relationships:
        load_options = build_recursive_load(model, max_depth=max_depth)
        for opt in load_options:
            stmt = stmt.options(opt)

    # ✅ Apply any custom options manually provided
    if options:
        for opt in options:
            stmt = stmt.options(opt)

    # Execute query
    result = await db.execute(stmt)
    items = result.scalars().all()

    # Total count
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
