import os
import asyncpg
from .models.base_case import base_case
from .models.users import User, hardcoded_users
from .models.accommodations import Accommodation, hardcoded_accommodations
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv()

#Get the login credential fron the env file and create a url for the database

DB_USERNAME = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

eng = create_async_engine(DATABASE_URL, echo=True)
LocalSession = sessionmaker(bind=eng, class_=AsyncSession, expire_on_commit=False)

#Function to setup database based on whether or not it already exists

async def setDataBase():
    adminConnection = await asyncpg.connect(user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database="postgres")
    try:
        exists = await adminConnection.fetchval("SELECT EXISTS(SELECT 1 FROM pg_database WHERE datname=$1)", DB_NAME)
        if not exists:
            await adminConnection.execute(f"DATABASE CREATED: {DB_NAME}")
            print(f"Created {DB_NAME}.")
        else:
            print(f"{DB_NAME} already exists.")
    finally:
        await adminConnection.close()

    async with eng.begin() as connection:
        await connection.run_sync(base_case.metadata.create_all)

async def populate_users():
    async with LocalSession() as session:
        async with session.begin():
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
        async with session.begin():
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
