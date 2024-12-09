from fastapi import APIRouter
from server.api.routers import supermarket_router,product_router

masterRouter = APIRouter()
masterRouter.include_router(supermarket_router.router, prefix="/supermarkets", tags=["Supermarkets"])
masterRouter.include_router(product_router.router, prefix="/products", tags=["Products"])