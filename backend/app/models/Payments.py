from sqlalchemy import Column, Integer, Float, DateTime, Text, ForeignKey, Enum, text
from sqlalchemy.orm import relationship

from app.db import Base
from .enums.payment_methods import PaymentMethod

class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float)
    date_paid = Column(DateTime)
    payment_method = Column(Enum(PaymentMethod, name="paymentmethods"), nullable=False, default=PaymentMethod.CASH)
    remarks = Column(Text)
    enrollment_id = Column(Integer, ForeignKey("enrollments.enrollment_id"))

    # Many-to-One: many payments -> one enrollment
    enrollment = relationship("Enrollments", back_populates="payments")

    def __repr__(self):
        return f"<Payment(amount={self.amount}, method={self.payment_method})>"