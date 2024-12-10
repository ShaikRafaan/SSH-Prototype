from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from server.models.base_case import  base_case as Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,unique=True)
    name = Column(String(20), index=True,unique=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"))

    supermarket = relationship("Supermarket", back_populates="products")
