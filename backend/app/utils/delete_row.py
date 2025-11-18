from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import select, func, inspect, desc

from fastapi import HTTPException


# got tired created this ... T_T
# don't judge me, as to why i didn't do this earlier
async def delete_by_id(db: AsyncSession, model, data_id: int):
    # Dynamically get primary key column
    pk_column = inspect(model).primary_key[0]

    # Query the item
    stmt = select(model).where(pk_column == data_id)
    result = await db.execute(stmt)
    obj = result.scalar_one_or_none()

    if obj is None:
        raise HTTPException(404, f"{model.__name__} with ID {data_id} not found")

    await db.flush(obj)
    await db.commit()

    return {"detail": "Deleted successfully"}