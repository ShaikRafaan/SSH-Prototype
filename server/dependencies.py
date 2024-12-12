from .database import LocalSession
from server.logging_config import setup_logging 

logger = setup_logging()

async def get_db():
    try:
        logger.info("Fetching new database session...")
        async with LocalSession() as database_session:
            logger.info("Database session created successfully.")
            yield database_session
    except Exception as e:
        logger.error("Error while creating database session.", exc_info=True)
        raise
