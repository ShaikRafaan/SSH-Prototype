import pytest
import asyncpg
import os

@pytest.mark.asyncio
async def test_database_connection():
    """
    Test if the application can connect to the database.

    This test attempts to establish a connection to the database
    using credentials from environment variables. If the connection
    succeeds, the test passes. Otherwise, it fails with an appropriate error.
    """

    # Fetch database connection details from environment variables
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = int(os.getenv("DB_PORT", 5432))
    # Construct a database URL (used in other libraries, but not needed for asyncpg)
    db_url = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    try:
         # Attempt to establish a connection to the database using asyncpg
        connection = await asyncpg.connect(
            user=db_user,
            password=db_password,
            database=db_name,
            host=db_host,
            port=db_port,
            url=db_url
        )
        # Ensure the connection is not None, indicating success
        assert connection is not None, "Failed to connect to the database"
        # Close the connection after successful connection
        await connection.close()
    except Exception as e:
         # If an exception occurs, fail the test with the error message
        pytest.fail(f"Database connection test failed: {e}")