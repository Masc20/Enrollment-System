from pydantic import BaseModel, ConfigDict

from typing import Optional


class TeacherBase(BaseModel):
    firstname: str
    lastname: str
    contact_number: str
    email: str

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(TeacherBase):
    pass

class TeacherOut(TeacherBase):
    teacher_id: int
    model_config = ConfigDict(from_attributes=True)