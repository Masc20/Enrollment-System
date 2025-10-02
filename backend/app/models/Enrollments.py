from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Enrollments(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)
    academic_year = Column(String(10))
    semester = Column(String(10))
    year_level = Column(String(10))
    student_id = Column(Integer, ForeignKey("students.student_id"))
    section_id = Column(Integer, ForeignKey("sections.section_id"), nullable=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    # Many-to-One: many enrollments -> one student
    student = relationship("Students", back_populates="enrollments")

    # Many-to-One: many enrollments -> one section
    section = relationship("Sections", back_populates="enrollments")

    # Many-to-One: many enrollments -> one course
    course = relationship("Courses", back_populates="enrollments")

    # One-to-Many: one enrollment -> many enrollment_details
    enrollment_details = relationship("EnrollmentDetails", back_populates="enrollment")

    # One-to-Many: one enrollment -> many payments
    payments = relationship("Payments", back_populates="enrollment")