from backend.app.db import engine

async def get_db():
    async with engine as session:
        yield session
