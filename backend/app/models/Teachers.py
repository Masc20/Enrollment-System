from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base

class Teachers(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    contact_number = Column(Integer)
    email = Column(String(50), unique=True)

    # One-to-Many: one teacher -> many schedules
    schedules = relationship("Schedules", back_populates="teacher")