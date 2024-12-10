from sqlalchemy import Column, Integer, String, Float
from server.models.base_case import base_case as Base

class Supermarket(Base):
    __tablename__ = "supermarkets"
    id = Column(Integer, primary_key=True,unique=True)
    name = Column(String(20),unique=True)
    location = Column(String(40), unique=False)
