from pydantic import BaseModel

class ProductBase(BaseModel):
   
    name: str
    price: str
    in_stock: str

class ProductCreate(BaseModel):
   
    supermarket_id: int

class Product(BaseModel):
   
    product_id: int
    name: str
    price: int
    in_stock: str
    supermarket_id: int


    class Config:
        orm_mode = True
