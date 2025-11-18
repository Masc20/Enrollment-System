from pydantic import BaseModel, ConfigDict

from typing import Optional

class GradeBase(BaseModel):
    grade: int
    remarks: str
    enroll_detail_id: int

class GradeCreate(GradeBase):
    remarks: Optional[str] = "No remarks"

class GradeUpdate(BaseModel):
    grade: Optional[int] = None
    remarks: Optional[str] = None
    enroll_detail_id: Optional[int] = None

class GradeOut(GradeBase):
   model_config = ConfigDict(from_attributes=True)