from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.v1 import students_api, sections_api, courses_api, departments_api, enrollment_api
from app.db import init_db

@asynccontextmanager
async def lifespan(apps: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown (if needed, e.g., close connections)

app = FastAPI(title="Enrollment System API", lifespan=lifespan)

# Register routers
app.include_router(students_api.router, prefix="/students", tags=["students"])
app.include_router(sections_api.router, prefix="/sections", tags=["sections"])
app.include_router(courses_api.router, prefix="/courses", tags=["courses"])
app.include_router(departments_api.router, prefix="/departments", tags=["departments"])
app.include_router(enrollment_api.router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Enrollment System"}

