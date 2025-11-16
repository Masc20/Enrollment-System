from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import date


class StudentRequirementBase(BaseModel):
    status: str     # submitted or not submitted
    date_submitted: date

class StudentRequirementCreate(BaseModel):
    status: str = "not submitted"   # default
    date_submitted: Optional[date] = None
    stud_id: int
    stud_req_id: int

class StudentRequirementUpdate(BaseModel):
    status: str = "submitted"
    date_submitted: date

class StudentRequirementOut(BaseModel):
    stud_req_id: int
    model_config = ConfigDict(from_attributes=True)