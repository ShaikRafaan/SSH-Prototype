from sqlalchemy import Column, Integer, String
from .base_case import base_case as Base

class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
