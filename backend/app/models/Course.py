from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.db import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    # 🔹 Relationship (1 course → many enrollments)
    enrollments = relationship("Enrollment", back_populates="course")
