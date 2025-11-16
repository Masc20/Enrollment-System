from pydantic import BaseModel, ConfigDict

from typing import Optional

from .department_schema import DepartmentOut

class CourseBase(BaseModel):
    course_name: str
    course_code: str

class CourseCreate(CourseBase):
    dept_id: Optional[int] = None
    dept_name: Optional[str] = None
    pass

class CourseUpdate(CourseBase):
    pass

class CourseOut(CourseBase):
    course_id: int
    department: DepartmentOut
    model_config = ConfigDict(from_attributes=True)

class PaginatedCourses(BaseModel):
    page: int
    limit: int
    total_courses: int
    total_pages: int
    courses: list[CourseOut]