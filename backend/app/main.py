from fastapi import FastAPI
from app.api.v1 import students

app = FastAPI(title="Enrollment System API")

# Register routers
app.include_router(students.router, prefix="/students", tags=["students"])
# app.include_router(courses.router, prefix="/courses", tags=["courses"])
# app.include_router(enrollment.router, prefix="/enrollment", tags=["enrollment"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Enrollment System"}
