from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Subjects(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    sub_code = Column(String(10))
    subject_name = Column(String(50))
    sub_type = Column(String(30))  # GenEd, Major, Elective
    num_units = Column(Integer)
    pre_req_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=True)

    # Self-reference: one subject -> many subjects (prerequisites)
    prerequisite = relationship("Subjects", remote_side=[subject_id])

    # One-to-Many: one subject -> many schedules
    schedules = relationship("Schedules", back_populates="subject")