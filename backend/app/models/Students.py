from sqlalchemy import Column, Integer, String, Text, Date, Enum
from sqlalchemy.orm import relationship

from app.db import Base

class Students(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_number = Column(String(30), unique=True)
    first_name = Column(String(30))
    middle_name = Column(String(30))
    last_name = Column(String(30))
    birth_date = Column(Date)
    gender = Column(String(30))
    contact_number = Column(String(15))
    email = Column(String(50), unique=True)
    address = Column(Text)
    admission_status = Column(String(30))           
    enrollment_status = Column(Enum("Regular", "Irregular"))          # regular, irregular
    student_type = Column(Enum("Old", "New", "Transferee"))           # old, new, transferee

    # One-to-Many: one student -> many enrollments
    enrollments = relationship("Enrollments", back_populates="student")

    # One-to-Many: one student -> many requirements
    requirements = relationship("StudentRequirements", back_populates="student")

    def __repr__(self):
        return f"<Student(name={self.first_name} {self.last_name})>"