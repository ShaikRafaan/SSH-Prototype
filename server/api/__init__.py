from fastapi import APIRouter
from .routers import userRouter
from .routers import accommodationRouter

masterRouter = APIRouter()
masterRouter.include_router(userRouter, prefix="/users", tags=["users"])
masterRouter.include_router(accommodationRouter, prefix="/accommodations", tags="[accommodations]") 