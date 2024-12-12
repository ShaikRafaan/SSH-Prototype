#from .product_router import router as ProductRouter
from .supermarket_router import router as SupermarketRouter
from .users import router as userRouter
from .product_router import router as ProductRouter
from .accommodations import router as accommodationRouter
from .order_management import router as OrderRouter
from fastapi import APIRouter

routersRouter = APIRouter()

routersRouter.include_router(ProductRouter)
routersRouter.include_router(SupermarketRouter)
routersRouter.include_router(userRouter)
routersRouter.include_router(accommodationRouter)
routersRouter.include_router(OrderRouter)