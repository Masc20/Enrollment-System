from sqlalchemy import Column, Integer, String, ForeignKey, Enum, text
from sqlalchemy.orm import relationship

from app.db import Base
from .enums.academics import YearLevel, Semesters

class Enrollments(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    academic_year = Column(String(10))
    semester = Column(Enum(Semesters, name="semesters"), nullable=False, default=Semesters.FIRST_SEM)
    year_level = Column(Enum(YearLevel, name="yearlevel"), nullable=False, default=YearLevel.FIRST)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    section_id = Column(Integer, ForeignKey("sections.section_id"), nullable=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    # --- Relationships ---
    # Many-to-One: many enrollments -> one student
    student = relationship(
        "Students",
        back_populates="enrollments",
        lazy="selectin"   # ✅ async-safe eager loading
    )

    # Many-to-One: many enrollments -> one section
    section = relationship(
        "Sections",
        back_populates="enrollments",
        lazy="selectin"
    )

    # Many-to-One: many enrollments -> one course
    course = relationship(
        "Courses",
        back_populates="enrollments",
        lazy="selectin"
    )

    # One-to-Many: one enrollment -> many enrollment_details
    enrollment_details = relationship(
        "EnrollmentDetails",
        back_populates="enrollment",
        lazy="selectin"
    )

    # One-to-Many: one enrollment -> many payments
    payments = relationship(
        "Payments",
        back_populates="enrollment",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Enrollment(year={self.academic_year}, sem={self.semester})>"