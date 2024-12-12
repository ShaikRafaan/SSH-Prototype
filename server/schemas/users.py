from pydantic import BaseModel


class UserCreate(BaseModel):
    firstname: str
    secondname: str
    email: str
    password: str

class UserRead(BaseModel):
    id: str
    firstname: str
    secondname: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    firstname: str
    secondname: str
    email: str
    password: str
    
    class Config:
        orm_mode = True