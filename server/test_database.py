import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv

load_dotenv()
# Fetch database connection details from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", 5432)
# Construct a database URL (used in other libraries, but not needed for asyncpg)
db_url = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_async_engine(db_url, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def run_test_query():
    """
    Run a SELECT 1 query to test the database connection.
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        value = result.scalar()  # Extract scalar value from result
        return value
    

@pytest.mark.asyncio
async def test_database_connection():
    """
    Test if the application can connect to the database.

    This test attempts to establish a connection to the database
    using credentials from environment variables. If the connection
    succeeds, the test passes. Otherwise, it fails with an appropriate error.
    """
    try:
        value = await run_test_query()
        assert value == 1, f"Unexpected query result: {value}"
    except Exception as e:
        pytest.fail(f"Database connection test failed: {e}")