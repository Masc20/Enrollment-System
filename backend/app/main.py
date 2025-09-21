from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.deps import get_db

app = FastAPI()

@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text('SELECT 1'))
        return {"status": "✅ Database connected!", "result": result.scalar()}
    except Exception as e:
        return {"status": "❌ Database connection failed", "error": str(e)}
