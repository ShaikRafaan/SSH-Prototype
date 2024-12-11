from pydantic import BaseModel

class AccommodationCreate(BaseModel):
    address: str

class AccommodationUpdate(BaseModel):
    address: str

class AccommodationResponse(BaseModel):
    id: str
    address: str

    class Config:
        orm_mode = True
