from pydantic import BaseModel, ConfigDict

from typing import Optional

from .department_schema import DepartmentOut

class CourseBase(BaseModel):
    course_name: str
    course_code: str
    dept_id: int

class CourseCreate(CourseBase):
    dept_id: Optional[int]
    dept_name: Optional[str]
    

class CourseUpdate(BaseModel):
    course_name: Optional[str]
    course_code: Optional[str]
    dept_id: Optional[int]

class CourseDelete(BaseModel):
    course_id: int

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