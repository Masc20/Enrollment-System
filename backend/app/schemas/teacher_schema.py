from pydantic import BaseModel, ConfigDict

from typing import Optional


class TeacherBase(BaseModel):
    firstname: str
    lastname: str
    contact_number: str
    email: str

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None

class TeacherOut(TeacherBase):
    teacher_id: int
    model_config = ConfigDict(from_attributes=True)

class PaginatedTeacherOut(BaseModel):
    page: int
    limit: int
    total_teachers: int
    total_pages: int
    teachers: list[TeacherOut]