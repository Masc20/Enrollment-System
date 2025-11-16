from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

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
    description="""
# 📘 Enrollment System API  
Welcome to the **Enrollment System** backend service.

This API provides:
- 👨‍🎓 Student Management  
- 🏫 Course & Departments  
- 📚 Enrollment Processing  

---

### 🔧 Tech Used:
- FastAPI  
- SQLAlchemy Async  
- PostgreSQL  
- Pytest for testing  
""",
    debug=True, 
    lifespan=lifespan
)

# -----------------------------------------
# ✅ Enable CORS Here
# -----------------------------------------
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------
# Register Routers
# -----------------------------------------
app.include_router(students_api.router, prefix="/students", tags=["students"])
app.include_router(sections_api.router, prefix="/sections", tags=["sections"])
app.include_router(courses_api.router, prefix="/courses", tags=["courses"])
app.include_router(departments_api.router, prefix="/departments", tags=["departments"])
app.include_router(enrollment_api.router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Enrollment System"}
