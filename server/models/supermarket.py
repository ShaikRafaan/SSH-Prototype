from sqlalchemy import Column, Integer, String, Float
from server.models.base_case import base_case as Base

class Supermarket(Base):
    __tablename__ = "supermarkets"
    supermarket_id = Column(Integer, primary_key=True,unique=True)
    supermarket_name = Column(String(20), unique=False, nullable=False)
    location = Column(String(40), unique=True, nullable=False)

hardcoded_supermarkets = [
    {
        "supermarket_id": 101,
        "supermarket_name": "FreshMart",
        "location": "123 Main St, Springfield"
    }
]