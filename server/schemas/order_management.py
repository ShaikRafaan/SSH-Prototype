from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
    product_name: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float
    items: List[OrderItemCreate]

    class Config:
        orm_mode = True

class OrderItemResponse(BaseModel):
    product_name: str
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: str
    customer_name: str
    total_amount: float
    items: List[OrderItemResponse]

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    customer_name: str
    total_amount: float

    class Config:
        orm_mode = True