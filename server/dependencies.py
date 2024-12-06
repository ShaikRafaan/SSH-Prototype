from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal
#Fetch a new database session for asynchronus database operations
async def f_database_session():
    async with SessionLocal() as database_session:
        yield database_session