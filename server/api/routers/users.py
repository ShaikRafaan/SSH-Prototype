# server/api/routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from server.schemas.users import UserCreate, UserRead, UserUpdate
from server.models.users import User
from server.dependencies import f_database_session

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: AsyncSession = Depends(f_database_session)):
    new_user = User(**user.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
    """return UserCreate(
        id="2435",
        firstname="John",
        lastname="A",
        email="john@gmail.com",
        password="johnpass"

    )"""


@router.get("/", response_model=List[UserRead])
async def list_users(db: AsyncSession = Depends(f_database_session)):
    """result = await db.execute(select(User))
    users = result.scalars().all()
    return users"""
    return

@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(f_database_session)):
    """result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user"""
    return

@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(f_database_session)):
    """result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user"""
    return

@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: AsyncSession = Depends(f_database_session)):
    """result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"detail": "User deleted successfully"}"""
    return
