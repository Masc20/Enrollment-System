from pydantic import BaseModel

from typing import Optional

class EnrollmentBase(BaseModel):
    academic_year: str
    semester: str
    year_level: str

class EnrollmentCreate(EnrollmentBase):

    # For Student
    student_id: Optional[int] = None
    student_number: Optional[str] = None

    # For Section
    section_id: Optional[int] = None
    section_name: Optional[str] = None

    # For Course
    course_id: Optional[int] = None
    course_code: Optional[str] = None

class EnrollmentUpdate(EnrollmentBase):
    pass

class EnrollmentOut(EnrollmentBase):
    enrollment_id: int

    class Config:
        from_attributes = True

class EnrollmentPaginated(BaseModel):
    pass