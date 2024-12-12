from pydantic import BaseModel

class AccommodationCreate(BaseModel):
    address: str

class AccommodationUpdate(BaseModel):
    address: str

class AccommodationResponse(BaseModel):
    id: int
    address: str
    city: str
    contact_number: str

    class Config:
        orm_mode = True
