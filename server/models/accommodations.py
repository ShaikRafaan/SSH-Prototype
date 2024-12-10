from sqlalchemy import Column, Integer, String
from .base_case import base_case as Base

class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer(15), primary_key=True, unique=True, nullable=False)
    name = Column(String(20), nullable=False)
    address = Column(String(40), nullable=False)
    city = Column(String(15), nullable=False)
    contact_number = Column(String(15), nullable=False, unique=True)
