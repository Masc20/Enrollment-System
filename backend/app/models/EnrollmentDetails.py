from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class EnrollmentDetails(Base):
    __tablename__ = "enrollment_details"

    enroll_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.enrollment_id"))
    schedule_id = Column(Integer, ForeignKey("schedules.schedule_id"))

    # Many-to-One: many enrollment_details -> one enrollment
    enrollment = relationship("Enrollments", back_populates="enrollment_details")

    # Many-to-One: many enrollment_details -> one schedule
    schedule = relationship("Schedules", back_populates="enrollment_details")

    # One-to-Many: one enrollment_detail -> many grades
    grades = relationship("Grades", back_populates="enrollment_detail")

    def __repr__(self):
        return f"<EnrollmentDetail(id={self.enroll_detail_id})>"