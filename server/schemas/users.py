from pydantic import BaseModel


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    firstname: str
    lastname: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    
    class Config:
        orm_mode = True