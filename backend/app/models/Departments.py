from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Departments(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(50))

    # One-to-Many: one department → many courses
    course = relationship("Courses", back_populates="department")