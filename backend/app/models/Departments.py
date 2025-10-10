from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(50), nullable=False)

    # One-to-Many: one department -> many courses
    courses = relationship("Courses", back_populates="department")

    def __repr__(self):
        return f"<Department(name={self.dept_name})>"
