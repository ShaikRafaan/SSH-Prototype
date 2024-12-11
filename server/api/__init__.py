from fastapi import APIRouter
from .routers import OrderRouter, userRouter

masterRouter = APIRouter()
masterRouter.include_router(userRouter, prefix="/users", tags=["users"])
masterRouter.include_router(OrderRouter, prefix="/ordermanagements", tags=["OrderManagement"])