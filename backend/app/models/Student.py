from sqlalchemy import Column, Integer, String, DateTime, Numeric, Text, func
from sqlalchemy.orm import relationship
from backend.app.db import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    student_number = Column(String)

    # 🔹 Relationship (1 student → many enrollments)
    enrollments = relationship("Enrollment", back_populates="student")
