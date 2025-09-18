

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.deps import get_db


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}
