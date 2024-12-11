from fastapi import APIRouter
from server.api.routers import supermarket_router,product_router,userRouter,accommodationRouter,OrderRouter
masterRouter = APIRouter()
masterRouter.include_router(supermarket_router.router, prefix="/supermarkets", tags=["Supermarkets"])
masterRouter.include_router(product_router.router, prefix="/products", tags=["Products"])
masterRouter.include_router(userRouter, prefix="/users", tags=["users"])
masterRouter.include_router(accommodationRouter, prefix="/accommodations", tags=["accommodations"]) 
masterRouter.include_router(OrderRouter, prefix="/ordermanagements", tags=["OrderManagement"])