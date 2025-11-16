from pydantic import BaseModel, ConfigDict

from typing import Optional

from .student_schema import EnrolledStudentOut
from .section_schema import EnrolledSectionOut
from .course_schema import CourseOut


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
    student: EnrolledStudentOut
    section: EnrolledSectionOut
    course: CourseOut
    model_config = ConfigDict(from_attributes=True)

class EnrollmentRelatedDataOut(EnrollmentBase):
    enrollment_id: int
    student: EnrolledStudentOut
    section: EnrolledSectionOut
    course: CourseOut
    model_config = ConfigDict(from_attributes=True)


class EnrollmentPaginated(BaseModel):
    page: int
    limit: int
    total_enrollments: int
    total_pages: int
    enrollments: list[EnrollmentRelatedDataOut]