from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

from .section_schema import SectionOut


# Shared properties
class StudentBase(BaseModel):
    student_number: Optional[str] = None
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    birth_date: date
    gender: str
    contact_number: Optional[str] = None
    email: EmailStr
    address: Optional[str] = None
    admission_status: str               # default{new}, old, transferee
    enrollment_status: str              # regular, irregular


# For creating a student (no ID yet)
class StudentCreate(StudentBase):
    pass


# For updating a student (all optional for patching)
class StudentUpdate(BaseModel):
    student_number: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    admission_status: Optional[str] = None
    enrollment_status: Optional[str] = None


# TO DO:
# create an authentication for the enrolled
# students so that the can update/remove info
class StudentAuth(StudentBase):
    pass

# What you return to clients (includes ID)
class StudentOut(StudentBase):
    student_id: int

    class Config:
        from_attributes = True

class FullStudentInformation(StudentOut):
    sections: SectionOut

class PaginatedStudents(BaseModel):
    page: int
    limit: int
    total_students: int
    total_pages: int
    students: list[StudentOut]


# TO DO:
# add a with the student and its related infos