from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_code = Column(String(30))
    course_name = Column(String(100))

    dept_id = Column(Integer, ForeignKey('departments.dept_id'), onupdate='CASCADE')

    # Many-to-One: many courses -> one department
    department = relationship("Departments", back_populates="courses")

    # One-to-Many: one courses -> many sections
    sections = relationship("Sections", back_populates="course")

    # One-to-Many: one course -> many enrollments
    enrollments = relationship("Enrollments", back_populates="course")


