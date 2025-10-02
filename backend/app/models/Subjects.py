from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Subjects(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_code = Column(String(100))
    subject_name = Column(String(100))
    subject_type = Column(String(100))      # GenEd, Major, Elective
    num_units  = Column(Integer)

    # allow null for those subjects with no prerequisite/s
    pre_req_id = Column(Integer, ForeignKey("subject.subject_id"), nullable=True)

    # One-to-One or Many: one subject -> one or many prerequisite/s
    prerequisite = relationship("Subjects", remote_side=[subject_id])

    # One-to-Many: one subject -> many schedules
    schedules = relationship("Schedules", back_populates="subject")