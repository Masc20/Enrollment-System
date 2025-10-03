from typing import Optional

from pydantic import BaseModel
from datetime import date


class StudentRequirement(BaseModel):
    status: str     # submitted or not submitted
    date_submitted: date

class StudentRequirementCreate(BaseModel):
    status: str = "not submitted"   # default
    date_submitted: Optional[date]
    stud_id: int
    req_id: int

class StudentRequirementUpdate(BaseModel):
    status: str = "submitted"
    date_submitted: date

class StudentRequirementOut(BaseModel):
    stud_req_id: int

    class Config:
        from_attributes = True