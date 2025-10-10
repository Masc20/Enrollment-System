from pydantic import BaseModel

from typing import Optional

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

    class Config:
        from_attributes = True