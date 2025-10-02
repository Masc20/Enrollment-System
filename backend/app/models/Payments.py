from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float)
    date_paid = Column(DateTime)
    payment_method = Column(String(30))
    remarks = Column(Text)
    enrollment_id = Column(Integer, ForeignKey("enrollments.enrollment_id"))

    # Many-to-One: many payments -> one enrollment
    enrollment = relationship("Enrollments", back_populates="payments")