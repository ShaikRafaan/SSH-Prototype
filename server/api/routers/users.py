from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.users import User
from server.schemas.users import UserResponse as UserSchema
from server.dependencies import get_db

router = APIRouter()

@router.get("/all", response_model=List[UserRead])
async def fetch_all_users(db: AsyncSession = Depends(get_db)) -> List[UserRead]:
    query_result = await db.execute(select(User))
    users = query_result.scalars().all()
    return [
        UserRead(
            user_id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email_id=user.email_id,
            phone_number=user.phone_number,
            accommodation_id=user.accommodation_id,
        )
        for user in users
    ]

@router.get("/{user_id}", response_model=UserRead)
async def fetch_user(user_id: str, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID '{user_id}' not found.")
    return UserRead(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        phone_number=user.phone_number,
        accommodation_id=user.accommodation_id,
    )

@router.post("/add", response_model=UserRead)
async def add_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    existing_user = await db.get(User, user_data.user_id)
    if existing_user:
        raise HTTPException(status_code=409, detail=f"User with ID '{user_data.user_id}' already exists.")

    user = User(
        user_id=user_data.user_id,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email_id=user_data.email_id,
        phone_number=user_data.phone_number,
        accommodation_id=user_data.accommodation_id,
    )
    db.add(user)
    await db.commit()
    return UserRead(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        phone_number=user.phone_number,
        accommodation_id=user.accommodation_id,
    )

@router.put("/update/{user_id}", response_model=UserRead)
async def update_user(user_id: str, user_data: UserUpdate, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID '{user_id}' not found.")

    user.first_name = user_data.first_name
    user.last_name = user_data.last_name
    user.email_id = user_data.email_id
    user.phone_number = user_data.phone_number
    user.accommodation_id = user_data.accommodation_id

    await db.commit()
    return UserRead(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        phone_number=user.phone_number,
        accommodation_id=user.accommodation_id,
    )

@router.delete("/delete/{user_id}", response_model=UserRead)
async def delete_user(user_id: str, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID '{user_id}' not found.")

    await db.delete(user)
    await db.commit()
    return UserRead(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        phone_number=user.phone_number,
        accommodation_id=user.accommodation_id,
    )

