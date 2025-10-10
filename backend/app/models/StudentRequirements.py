from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class StudentRequirements(Base):
    __tablename__ = "student_requirements"

    stud_req_id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(10))
    date_submitted = Column(DateTime)
    stud_id = Column(Integer, ForeignKey("students.student_id"))
    req_id = Column(Integer, ForeignKey("requirements.req_id"))

    # Many-to-One: many student_requirements -> one student
    student = relationship("Students", back_populates="requirements")

    # Many-to-One: many student_requirements -> one requirement
    requirement = relationship("Requirements", back_populates="student_requirements")

    def __repr__(self):
        return f"<StudentRequirement(status={self.status})>"