from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import HTTPException

from app.models.StudentRequirements import StudentRequirements

from app.schemas.studentRequirement_sch import *




async def add_students_requirements(
        db: AsyncSession, 
        student_id: int, 
        req_id: int
        ) -> StudentRequirements:

    result = await db.execute(select(StudentRequirements)
                              .where(
                                  (StudentRequirements.stud_id == student_id) &
                                  (StudentRequirements.req_id == req_id)
                                     )
                              )    

    isAdded = result.scalar_one_or_none()

    if isAdded:
        raise HTTPException(status_code=422, detail="The requirement is already added")
    
    