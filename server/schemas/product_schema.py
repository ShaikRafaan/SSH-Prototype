from pydantic import BaseModel

class ProductBase(BaseModel):
   
    name: str
    price: str
    in_stock: str

class ProductCreate(BaseModel):
   
    supermarket_id: str

class Product(BaseModel):
   
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True
