

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.migrations import run_migrations
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # 🔹 Run migrations automatically
    run_migrations()
    print("✅ Database migrations applied!")

@app.get("/")
async def root():
    return {"message": "Hello, world!"}


