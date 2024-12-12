from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base_case import base_case as Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    total_amount = Column(Float)

    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order", back_populates="items")

hardcoded_orders = [
    {"id": 1, "customer_name": "Alice", "total_amount": 150.50, "items": [
        {"id": 1, "product_name": "Laptop", "quantity": 1, "price": 150.50}
    ]},
    {"id": 2, "customer_name": "Bob", "total_amount": 85.00, "items": [
        {"id": 2, "product_name": "Headphones", "quantity": 2, "price": 42.50}
    ]},
    {"id": 3, "customer_name": "Charlie", "total_amount": 200.00, "items": [
        {"id": 3, "product_name": "Monitor", "quantity": 2, "price": 100.00}
    ]},
    {"id": 4, "customer_name": "Diana", "total_amount": 45.00, "items": [
        {"id": 4, "product_name": "Keyboard", "quantity": 1, "price": 45.00}
    ]},
    {"id": 5, "customer_name": "Ethan", "total_amount": 25.00, "items": [
        {"id": 5, "product_name": "Mouse", "quantity": 1, "price": 25.00}
    ]},
    {"id": 6, "customer_name": "Fiona", "total_amount": 300.00, "items": [
        {"id": 6, "product_name": "Chair", "quantity": 2, "price": 150.00}
    ]},
    {"id": 7, "customer_name": "George", "total_amount": 120.00, "items": [
        {"id": 7, "product_name": "Desk", "quantity": 1, "price": 120.00}
    ]},
    {"id": 8, "customer_name": "Hannah", "total_amount": 75.00, "items": [
        {"id": 8, "product_name": "Lamp", "quantity": 3, "price": 25.00}
    ]},
    {"id": 9, "customer_name": "Ian", "total_amount": 60.00, "items": [
        {"id": 9, "product_name": "Book", "quantity": 4, "price": 15.00}
    ]},
    {"id": 10, "customer_name": "Jane", "total_amount": 90.00, "items": [
        {"id": 10, "product_name": "Backpack", "quantity": 1, "price": 90.00}
    ]}
]
