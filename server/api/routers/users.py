from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.users import User
from server.schemas.users import UserResponse as UserSchema
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=UserSchema)
async def list_users() -> UserSchema:    
    return UserSchema(
        id= "12345",
        firstname= "John",
        lastname= "Doe",
        email= "john.doe@example.com"
    )

@router.post("/add", response_model=UserSchema)
async def add_user(user: UserSchema, db: AsyncSession = Depends(get_db)) -> UserSchema:

    return UserSchema(
        id="new-id",
        firstname= "new-fname",
        lastname= "new-lname",
        email= "new-email"
    )


@router.get("/search/{id}", response_model=list[UserSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):
    if id == "12345":
        return [UserSchema(id="12345", firstname="John", lastname="Doe", email="john.doe@example.com")]
    else:
        return []

@router.delete("/delete/{user_id}", response_model=dict)
async def delete_user(user_id: str, db: AsyncSession = Depends(get_db)) -> dict:

    if user_id == "12345":
        return {"message": f"user with ID {user_id} has been deleted."}
    else:
        return {"message": f"user with ID {user_id} does not exist."}


@router.put("/update/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int,update_data: UserSchema,db: AsyncSession = Depends(get_db)) -> UserSchema:

    if user_id == 12345:
        return UserSchema(
            id="12345",
            firstname=update_data.firstname or "Updated Fname",
            lastname=update_data.lastname or "Updated Lname",
            email=update_data.email or "Updated email"
        )
    else:
        return UserSchema(
            id=str(user_id),
            firstname="Non-existent user (for testing purposes)",
            lastname="Non-existent user (for testing purposes)",
            email="Non-existent user (for testing purposes)"
        )
