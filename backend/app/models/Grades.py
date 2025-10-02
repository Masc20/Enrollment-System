from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Grades(Base):
    __tablename__ = "grades"

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(DECIMAL(3, 2))
    remarks = Column(String(30))
    enroll_detail_id = Column(Integer, ForeignKey("enrollment_details.enroll_detail_id"))

    # Many-to-One: many grades -> one enrollment_detail
    enrollment_detail = relationship("EnrollmentDetails", back_populates="grades")