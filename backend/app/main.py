

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}


