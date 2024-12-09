from fastapi import APIRouter
from .routers import userRouter

masterRouter = APIRouter()
masterRouter.include_router(userRouter, prefix="/users", tags=["users"]) 