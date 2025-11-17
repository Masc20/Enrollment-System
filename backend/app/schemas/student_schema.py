from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date


# Shared properties
class StudentBase(BaseModel):
    student_number: Optional[str]
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    birth_date: date
    gender: str
    contact_number: Optional[str] = "No Number Set"
    email: EmailStr
    address: Optional[str]
    admission_status: Optional[str] = "new"               # default{new}, old, transferee
    enrollment_status: str              # regular, irregular


# For creating a student (no ID yet)
class StudentCreate(StudentBase):
    pass


# For updating a student (all optional for patching)
class StudentUpdate(BaseModel):
    student_number: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[date]
    gender: Optional[str]
    contact_number: Optional[str] 
    email: Optional[EmailStr]
    address: Optional[str]
    admission_status: Optional[str]
    enrollment_status: Optional[str]

class StudentAuth(StudentBase):
    pass

# What you return to clients (includes ID)
class StudentOut(StudentBase):
    student_id: int
    model_config = ConfigDict(from_attributes=True)

class PaginatedStudents(BaseModel):
    page: int
    limit: int
    total_students: int
    total_pages: int
    students: list[StudentOut]

class EnrolledStudentOut(BaseModel):
    student_id: int
    student_number: str
    model_config = ConfigDict(from_attributes=True)

# TO DO:
# create an authentication for the enrolled
# students so that the can update/remove info
# add a with the student and its related infos