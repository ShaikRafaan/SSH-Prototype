import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv
from server.logging_config import setup_logging 

logger = setup_logging()

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", 5432)
db_url = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_async_engine(db_url, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def run_test_query():
    logger.info("Running test query to check database connection...")
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        value = result.scalar()
        logger.info(f"Test query result: {value}")
        return value

@pytest.mark.asyncio
async def test_database_connection():
    logger.info("Starting database connection test...")
    try:
        value = await run_test_query()
        assert value == 1, f"Unexpected query result: {value}"
        logger.info("Database connection test passed.")
    except Exception as e:
        logger.error(f"Database connection test failed: {e}", exc_info=True)
        pytest.fail(f"Database connection test failed: {e}")
