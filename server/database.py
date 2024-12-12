import os
import asyncpg
from .models.base_case import base_case
from .models.product import Product, hardcoded_products
from .models import Supermarket, hardcoded_supermarkets
from .models.users import User, hardcoded_users
from .models.accommodations import Accommodation, hardcoded_accommodations
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from server.logging_config import setup_logging 
from sqlalchemy import text
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

    async with eng.begin() as connection:
        await connection.run_sync(base_case.metadata.drop_all)
        await connection.run_sync(base_case.metadata.create_all)

async def populate_supermarkets(LocalSession):
    async with LocalSession() as session:
        for data in hardcoded_supermarkets:
            session.add(Supermarket(**data))
        await session.commit()
        print("Supermarkets table populated.")
    
async def populate_products():
    async with LocalSession() as session:
        for data in hardcoded_products:
            product = Product(
                id=data["id"],
                product_name=data["product_name"],
                price=data["price"],
                in_stock=data["in_stock"],
                supermarket_id=data["supermarket_id"]
            
             )
            session.add(product)
        await session.commit()
        print("Products table populated.")

async def populate_users():
    async with LocalSession() as session:
            for data in hardcoded_users:
                user = User(
                    id=data["id"],
                    first_name=data["first_name"],
                    second_name=data["second_name"],
                    email=data["email"],
                    password=data["password"],
                    accommodation_id=data["accommodation_id"]
                )
                session.add(user)
            await session.commit()
            print("Users table populated.")

async def populate_accommodations():
    async with LocalSession() as session:
            for data in hardcoded_accommodations:
                accommodation = Accommodation(
                    accommodation_id=data["accommodation_id"],
                    address=data["address"],
                    city=data["city"],
                    contact_number=data["contact_number"]
                )
                session.add(accommodation)
            await session.commit()
            print("Accommodations table populated.")

async def create_tables():
    await setDataBase()
    async with eng.begin() as connection:
        await connection.run_sync(base_case.metadata.create_all)
    await populate_products(LocalSession)
    await populate_accommodations(LocalSession)
    await populate_supermarkets(LocalSession)