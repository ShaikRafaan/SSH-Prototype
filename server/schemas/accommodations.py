from pydantic import BaseModel

class AccommodationCreate(BaseModel):
    name: str
    address: str

class AccommodationUpdate(BaseModel):
    name: str
    address: str

class AccommodationResponse(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True
