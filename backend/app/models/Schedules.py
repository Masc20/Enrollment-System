from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from app.db import Base
from .enums.days import Week

class Schedules(Base):
    __tablename__ = "schedules"

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    days = Column(Enum(Week, name="week"))
    sched_time = Column(DateTime)
    room_number = Column(String(10))
    section_id = Column(Integer, ForeignKey("sections.section_id"))
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"))
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))

    # Many-to-One: many schedules -> one section
    section = relationship("Sections", back_populates="schedules")

    # Many-to-One: many schedules -> one subject
    subject = relationship("Subjects", back_populates="schedules")

    # Many-to-One: many schedules -> one teacher
    teacher = relationship("Teachers", back_populates="schedules")

    # One-to-Many: one schedule -> many enrollment_details
    enrollment_details = relationship("EnrollmentDetails", back_populates="schedule")

    def __repr__(self):
        return f"<Schedule(id={self.schedule_id}, room={self.room_number})>"
