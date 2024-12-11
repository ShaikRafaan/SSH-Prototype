from fastapi import APIRouter
from .routers import OrderRouter

masterRouter = APIRouter()
masterRouter.include_router(OrderRouter, prefix="/ordermanagements", tags=["OrderManagement"])