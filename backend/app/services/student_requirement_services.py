from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from fastapi import HTTPException

from app.models.StudentRequirements import StudentRequirements
from app.utils.pagination import paginate_query
from app.schemas.student_requirement_schema import *

async def list_student_requirements(
    db: AsyncSession,
    page: int = 1,
    limit: int = None
):
    return await paginate_query(
        db=db,
        model=StudentRequirements,
        page=page,
        limit=limit,
        options=[
            selectinload(StudentRequirements.student),
            selectinload(StudentRequirements.requirement)
        ]
    )


# Filtered by students
async def list_student_requirements_by_student(
    db: AsyncSession,
    student_id: int,
    page: int = 1,
    limit: int = None
):
    stmt_options = [
        selectinload(StudentRequirements.student),
        selectinload(StudentRequirements.requirement)
    ]

    # Filtered pagination
    base_query = select(StudentRequirements).where(
        StudentRequirements.stud_id == student_id
    )

    return await paginate_query(
        db=db,
        model=StudentRequirements,
        page=page,
        limit=limit,
        options=stmt_options,
        auto_load_relationships=False 
    )


async def add_students_requirements(
        db: AsyncSession, 
        add_student_requirements: StudentRequirementCreate
):

    result = await db.execute(select(StudentRequirements)
                              .where(
                                  (StudentRequirements.stud_id == add_student_requirements.stud_id) &
                                  (StudentRequirements.req_id == add_student_requirements.req_id)
                                     )
                              )    

    isAdded = result.scalar_one_or_none()

    if isAdded:
        raise HTTPException(status_code=422, detail="The requirement is already added")
    
    db_student_requirements = StudentRequirements(
        req_id = add_student_requirements.req_id,
        stud_id = add_student_requirements.stud_id
    )
    
    db.add(db_student_requirements)
    await db.commit()
    await db.refresh(db_student_requirements)
    return db_student_requirements

async def update_status(
        db: AsyncSession,
        stud_req_id: int,
        update_data: StudentRequirementUpdate
):

    # Fetch the existing record
    result = await db.execute(
        select(StudentRequirements).where(
            StudentRequirements.stud_req_id == stud_req_id
        )
    )

    db_record = result.scalar_one_or_none()

    # Check if it exists
    if not db_record:
        raise HTTPException(
            status_code=404,
            detail=f"Student Requirement with ID {stud_req_id} not found"
        )

    # Update allowed fields
    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(db_record, key, value)

    # Save changes
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)

    return db_record