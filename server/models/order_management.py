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
