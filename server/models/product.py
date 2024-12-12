from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .supermarket import Supermarket
from .base_case import base_case as Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True,unique=True, nullable=False)
    product_name = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, nullable=False)
    supermarket_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"products(ID = {self.product_id}, Name = {self.product_name}, price = {self.price}, in Stock? ={self.in_stock}, supermarket Id ={Supermarket(self.supermarket_id)})>"
    


hardcoded_products = [
    {
        "product_id": 1,
        "product_name": "Apples",
        "price": 1.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 2,
        "product_name": "Bananas",
        "price": 0.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 3,
        "product_name": "Oranges",
        "price": 2.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 4,
        "product_name": "Milk",
        "price": 3.79,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 5,
        "product_name": "Bread",
        "price": 2.99,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 6,
        "product_name": "Eggs",
        "price": 4.29,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 7,
        "product_name": "Cheese",
        "price": 5.99,
        "in_stock": False,
        "supermarket_id": 101
    },
    {
        "product_id": 8,
        "product_name": "Butter",
        "price": 4.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 9,
        "product_name": "Yogurt",
        "price": 1.49,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 10,
        "product_name": "Chicken Breast",
        "price": 9.99,
        "in_stock": False,
        "supermarket_id": 101
    },
    {
        "product_id": 11,
        "product_name": "Pasta",
        "price": 2.79,
        "in_stock": True,
        "supermarket_id": 101
    },
    {
        "product_id": 12,
        "product_name": "Tomatoes",
        "price": 1.89,
        "in_stock": True,
        "supermarket_id": 101
    }
]
