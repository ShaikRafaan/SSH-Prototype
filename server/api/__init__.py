from fastapi import APIRouter
from .routers import userRouter,accommodationRouter,OrderRouter
masterRouter = APIRouter()
masterRouter.include_router(userRouter, prefix="/users", tags=["users"])
masterRouter.include_router(accommodationRouter, prefix="/accommodations", tags=["accommodations"]) 
masterRouter.include_router(OrderRouter, prefix="/ordermanagements", tags=["OrderManagement"])