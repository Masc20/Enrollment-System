from sqlalchemy import Column, Integer, String, Text, Enum

from app.db import Base
from .enums.admins import AdminRole

class Administrators (Base):
    __tablename__ = "administrators"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30))
    password = Column(Text)
    role = Column(Enum(AdminRole), nullable=False, name="adminrole") 