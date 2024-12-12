from fastapi import APIRouter
from .routers import SupermarketRouter, userRouter, accommodationRouter, OrderRouter, ProductRouter
masterRouter = APIRouter()
masterRouter.include_router(SupermarketRouter, prefix="/supermarkets", tags=["Supermarkets"])
masterRouter.include_router(ProductRouter, prefix="/products", tags=["Products"])
masterRouter.include_router(userRouter, prefix="/users", tags=["users"])
masterRouter.include_router(accommodationRouter, prefix="/accommodations", tags=["Accommodations"]) 
masterRouter.include_router(OrderRouter, prefix="/ordermanagements", tags=["OrderManagement"])