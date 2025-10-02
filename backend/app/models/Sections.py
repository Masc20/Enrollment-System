from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Sections(Base):
    __tablename__ = "sections"

    section_id = Column(Integer, primary_key=True)
    section_name = Column(String(30))
    year_level = Column(String(10))
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    # Many-to-One: many sections -> one course
    course = relationship("Courses", back_populates="sections")

    # One-to-Many: one section -> many schedules
    schedules = relationship("Schedules", back_populates="section")

    # One-to-Many: one section -> many enrollments
    enrollments = relationship("Enrollments", back_populates="section")