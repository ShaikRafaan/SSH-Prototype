import os
import asyncpg
from .models.base_case import base_case
from .models.product import Product, hardcoded_products
from .models.supermarket import Supermarket, hardcoded_supermarkets
from .models.users import User, hardcoded_users
from .models.accommodations import Accommodation, hardcoded_accommodations
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from server.logging_config import setup_logging 

load_dotenv()


logger = setup_logging()

DB_USERNAME = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


eng = create_async_engine(DATABASE_URL, echo=True)
LocalSession = sessionmaker(bind=eng, class_=AsyncSession, expire_on_commit=False)

async def setDataBase():
    logger.info("Attempting to connect to the PostgreSQL server...")

    adminConnection = await asyncpg.connect(user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database="postgres")
    try:
        logger.info(f"Checking if database {DB_NAME} exists...")
        exists = await adminConnection.fetchval("SELECT EXISTS(SELECT 1 FROM pg_database WHERE datname=$1)", DB_NAME)
        
        if not exists:
            logger.info(f"Database {DB_NAME} does not exist. Creating it...")
            await adminConnection.execute(f"CREATE DATABASE {DB_NAME}")
            logger.info(f"Created database {DB_NAME}.")
        else:
            logger.info(f"Database {DB_NAME} already exists.")
    except Exception as e:
        logger.error(f"Error while checking or creating database {DB_NAME}: {e}", exc_info=True)
    finally:
        await adminConnection.close()

    try:
        logger.info("Creating tables if not already present...")
        async with eng.begin() as connection:
            await connection.run_sync(base_case.metadata.create_all)
        logger.info("Database tables created or already exist.")
    except Exception as e:
        logger.error("Error creating tables in the database.", exc_info=True)
