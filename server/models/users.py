from sqlalchemy import Column, Integer, String, ForeignKey
from .base_case import base_case as Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), nullable=False, unique=False)
    second_name = Column(String(20), nullable=False, unique=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    accommodation_id = Column(String(15), ForeignKey=True, nullable=False)


hardcoded_users = [
    {
        "id": 1,
        "first_name": "John",
        "second_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "accommodation_id": "ACC001"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "second_name": "Smith",
        "email": "jane.smith@example.com",
        "password": "securepass456",
        "accommodation_id": "ACC002"
    },
    {
        "id": 3,
        "first_name": "Alice",
        "second_name": "Johnson",
        "email": "alice.johnson@example.com",
        "password": "mypassword789",
        "accommodation_id": "ACC003"
    },
    {
        "id": 4,
        "first_name": "Bob",
        "second_name": "Brown",
        "email": "bob.brown@example.com",
        "password": "password321",
        "accommodation_id": "ACC004"
    },
    {"id": 5,
        "first_name": "Charlie",
        "second_name": "Davis",
        "email": "charlie.davis@example.com",
        "password": "passcharlie5",
        "accommodation_id": "ACC005"
    },
    {
        "id": 6,
        "first_name": "Emily",
        "second_name": "Evans",
        "email": "emily.evans@example.com",
        "password": "emily456pass",
        "accommodation_id": "ACC006"
    },
    {
        "id": 7,
        "first_name": "Frank",
        "second_name": "Green",
        "email": "frank.green@example.com",
        "password": "frank789",
        "accommodation_id": "ACC007"
    },
    {
        "id": 8,
        "first_name": "Grace",
        "second_name": "Harris",
        "email": "grace.harris@example.com",
        "password": "gracepass123",
        "accommodation_id": "ACC008"
    },
    {
        "id": 9,
        "first_name": "Henry",
        "second_name": "Irwin",
        "email": "henry.irwin@example.com",
        "password": "henrypass321",
        "accommodation_id": "ACC009"
    },
    {
        "id": 10,
        "first_name": "Isabel",
        "second_name": "Jackson",
        "email": "isabel.jackson@example.com",
        "password": "isabel789",
        "accommodation_id": "ACC010"
    }
]