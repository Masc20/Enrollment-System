from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    student_number = Column(String, unique=True, index=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    birth_date = Column(DateTime)
    gender = Column(String(20))
    contact_no = Column(String(16))
    email = Column(String, unique=True, index=True)
    address = Column(String)
    enrollment_status = Column(String(30))
