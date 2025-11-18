from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.enums.days import Week

class ScheduleBase(BaseModel):
    days: Week
    sched_time: datetime
    room_number: str
    section_id: int
    subject_id: int
    teacher_id: int


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(BaseModel):
    days: Optional[Week] = None
    sched_time: Optional[datetime] = None
    room_number: Optional[str] = None
    section_id: Optional[int] = None
    subject_id: Optional[int] = None
    teacher_id: Optional[int] = None


class ScheduleOut(ScheduleBase):
    schedule_id: int

    model_config = ConfigDict(from_attributes=True)
