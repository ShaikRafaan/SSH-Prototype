import os
import asyncpg
from .models.base_case import base_case
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