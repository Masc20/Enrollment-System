from pydantic import BaseModel

from typing import Optional

from .course_sch import CourseOut


class SectionBase(BaseModel):
    section_name: str
    year_level: str

class SectionCreate(SectionBase):
    # For Course
    course_id: Optional[int] = None
    course_code: Optional[str] = None
    course_name: Optional[str] = None

class SectionOut(SectionBase):
    section_id: int
    course: CourseOut

    class Config:
        from_attributes = True

class PaginatedSections(BaseModel):
    page: int
    limit: int
    total_sections: int
    total_pages: int
    sections: list[SectionOut]