from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date

from app.models.enums.students import AdmissionStatus, EnrollmentStatus, StudentType
from app.models.enums.gender import Gender


# Shared properties
class StudentBase(BaseModel):
    student_number: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    birth_date: date
    gender: Gender
    contact_number: Optional[str] = None
    email: EmailStr
    address: Optional[str] = None
    admission_status: Optional[AdmissionStatus] = AdmissionStatus.PENDING
    enrollment_status: EnrollmentStatus       
    student_type: Optional[StudentType] = StudentType.NEW   


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
    gender: Optional[Gender] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    admission_status: Optional[AdmissionStatus] = None
    enrollment_status: Optional[EnrollmentStatus] = None
    student_type: Optional[StudentType] = None

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