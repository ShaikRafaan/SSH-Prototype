from pydantic import BaseModel
from typing import List

class SupermarketBase(BaseModel):
    name: str
    location: str

class SupermarketCreate(BaseModel):
    pass

class Supermarket(BaseModel):
    id: int
    name: str
    location:str
    class Config:
        orm_mode = True

