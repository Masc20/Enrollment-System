from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.v1 import students_api, sections_api, courses_api, departments_api, enrollment_api
from app.db import init_db, engine

import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting up...")
        await init_db()
        yield
    finally:
        logger.info("Shutting down...")
        await engine.dispose()

app = FastAPI(
    title="Enrollment System API",
    debug=True, 
    lifespan=lifespan)

# Register routers
app.include_router(students_api.router, prefix="/students", tags=["students"])
app.include_router(sections_api.router, prefix="/sections", tags=["sections"])
app.include_router(courses_api.router, prefix="/courses", tags=["courses"])
app.include_router(departments_api.router, prefix="/departments", tags=["departments"])
app.include_router(enrollment_api.router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Enrollment System"}

