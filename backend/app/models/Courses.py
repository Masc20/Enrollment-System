from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Courses(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(10), nullable=False)
    course_name = Column(String(50), nullable=False)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    # Many-to-One: many courses -> one department
    department = relationship("Departments", back_populates="courses", lazy="selectin")

    # One-to-Many: one course -> many sections
    sections = relationship("Sections", back_populates="course", lazy="selectin")

    # One-to-Many: one course -> many enrollments
    enrollments = relationship("Enrollments", back_populates="course", lazy="selectin")

    def __repr__(self):
        return f"<Course(code={self.course_code}, name={self.course_name})>"
