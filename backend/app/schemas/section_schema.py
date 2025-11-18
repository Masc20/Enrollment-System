from pydantic import BaseModel, ConfigDict

from typing import Optional

from .course_schema import CourseOut
from app.models.enums.academics import YearLevel


class SectionBase(BaseModel):
    section_name: str
    year_level: YearLevel

class SectionCreate(SectionBase):
    # For Course
    course_id: Optional[int] = None
    course_code: Optional[str] = None
    course_name: Optional[str] = None

class SectionOut(SectionBase):
    section_id: int
    course: CourseOut
    model_config = ConfigDict(from_attributes=True)

class SectionUpdate(SectionBase):
    course_id: Optional[int] = None

class EnrolledSectionOut(SectionBase):
    section_id: int
    section_name : str


class PaginatedSections(BaseModel):
    page: int
    limit: int
    total_sections: int
    total_pages: int
    sections: list[SectionOut]