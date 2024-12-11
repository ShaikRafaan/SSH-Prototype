from sqlalchemy import Column, Integer, String
from .base_case import base_case as Base

class Accommodation(Base):
    __tablename__ = "accommodations"

    accommodation_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    address = Column(String(40), nullable=False)
    city = Column(String(15), nullable=False)
    contact_number = Column(String(15), nullable=False, unique=True)

hardcoded_accommodations = [
    {
        "accommodation_id": 1,
        "address": "1725 Slough Avenue",
        "city": "Scranton",
        "contact_number": "555-1234"
    },
    {
        "accommodation_id": 2,
        "address": "45 Maple Street",
        "city": "Scranton",
        "contact_number": "555-5678"
    },
    {
        "accommodation_id": 3,
        "address": "22 Oak Lane",
        "city": "Scranton",
        "contact_number": "555-8765"
    },
    {
        "accommodation_id": 4,
        "address": "Schrute Farms, Beet Lane",
        "city": "Honesdale",
        "contact_number": "555-4321"
    },
    {
        "accommodation_id": 5,
        "address": "73 Ivy Way",
        "city": "Stamford",
        "contact_number": "555-8764"
    },
    {
        "accommodation_id": 6,
        "address": "90 Willow Drive",
        "city": "Scranton",
        "contact_number": "555-2345"
    },
    {
        "accommodation_id": 7,
        "address": "301 Elm Street",
        "city": "Scranton",
        "contact_number": "555-6789"
    },
    {
        "accommodation_id": 8,
        "address": "67 Birch Lane",
        "city": "New York",
        "contact_number": "555-3456"
    },
    {
        "accommodation_id": 9,
        "address": "15 Pine Circle",
        "city": "Scranton",
        "contact_number": "555-9876"
    },
    {
        "accommodation_id": 10,
        "address": "123 Cat Lane",
        "city": "Scranton",
        "contact_number": "555-5432"
    }
]