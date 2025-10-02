from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Requirements(Base):
    __tablename__ = "requirements"

    req_id = Column(Integer, primary_key=True, autoincrement=True)
    req_name = Column(String(50))

    # One-to-Many: one requirement -> many student_requirements
    student_requirements = relationship("StudentRequirements", back_populates="requirement")