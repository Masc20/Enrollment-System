from sqlalchemy import Column, Integer, String, ForeignKey, Enum, text
from sqlalchemy.orm import relationship

from app.db import Base
from .enums.academics import YearLevel

class Sections(Base):
    __tablename__ = "sections"

    section_id = Column(Integer, primary_key=True, autoincrement=True)
    section_name = Column(String(30))
    year_level = Column(Enum(YearLevel, name="yearlevels"), nullable=False, default=YearLevel.FIRST)
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    # Relationships
    # Many-to-One: many sections -> one course
    course = relationship("Courses", back_populates="sections")

    # One-to-Many: one section -> many schedules
    schedules = relationship("Schedules", back_populates="section")

    # One-to-Many: one section -> many enrollments
    enrollments = relationship("Enrollments", back_populates="section")

    def __repr__(self):
        return f"<Section(name={self.section_name}, year_level={self.year_level})>"


