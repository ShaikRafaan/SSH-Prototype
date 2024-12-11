from .database import LocalSession
#Fetch a new database session for asynchronus database operations
async def get_db():
    async with LocalSession() as database_session:
        yield database_session
