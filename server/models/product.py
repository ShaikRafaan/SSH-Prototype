from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from server.models.base_case import  base_case as Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,unique=True)
    product_name = Column(String(20), index=True,unique=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"))

    supermarket = relationship("Supermarket", back_populates="products")


hardcoded_products = [
    {
        "id": 1,
        "product_name": "Apples",
        "price": 1.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 2,
        "product_name": "Bananas",
        "price": 0.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 3,
        "product_name": "Oranges",
        "price": 2.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 4,
        "product_name": "Milk",
        "price": 3.79,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 5,
        "product_name": "Bread",
        "price": 2.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 6,
        "product_name": "Eggs",
        "price": 4.29,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 7,
        "product_name": "Cheese",
        "price": 5.99,
        "in_stock": False,
        "supermarket_id": 101
    },
    {
        "id": 8,
        "product_name": "Butter",
        "price": 4.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 9,
        "product_name": "Yogurt",
        "price": 1.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 10,
        "product_name": "Chicken Breast",
        "price": 9.99,
        "in_stock": False,
        "supermarket_id": 101
    },
    {
        "id": 11,
        "product_name": "Pasta",
        "price": 2.79,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "id": 12,
        "product_name": "Tomatoes",
        "price": 1.89,
        "in_stock": True,
        "supermarket_id": 101
    }
]
