from pydantic import BaseModel, ConfigDict
from typing import Optional

class EnrollmentDetailBase(BaseModel):
    enrollment_id: int
    schedule_id: int

class EnrollmentDetailCreate(EnrollmentDetailBase):
    pass

class EnrollmentDetailUpdate(BaseModel):
    enrollment_id: Optional[int] = None
    schedule_id: Optional[int] = None

class EnrollmentDetailOut(EnrollmentDetailBase):
    enroll_detail_id: int
    model_config = ConfigDict(from_attributes=True)

class PaginatedEnrollmentDetail(BaseModel):
    page: int
    limit: int
    total_details: int
    total_pages: int
    details: list[EnrollmentDetailOut]