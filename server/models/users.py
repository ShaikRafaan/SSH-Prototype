from sqlalchemy import Column, Integer, String
from .base_case import base_case as Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    accommodation_id = Column(String(15), foreign_key=True, nullable=False)