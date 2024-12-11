from pydantic import BaseModel

class SupermarketBase(BaseModel):
    name: str
    location: str

class SupermarketCreate(BaseModel):
    pass

class Supermarket(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
