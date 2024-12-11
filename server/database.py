import os
import asyncpg
from .models.base_case import base_case
from .models.product import Product, hardcoded_products
from .models.supermarket import Supermarket, hardcoded_supermarkets
from .models.users import User, hardcoded_users
from .models.accommodations import Accommodation, hardcoded_accommodations
from .models.order_management import Order, OrderItem, hardcoded_orders
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
        await connection.run_sync(base_case.metadata.drop_all)
        await connection.run_sync(base_case.metadata.create_all)

async def populate_supermarkets():
    async with LocalSession() as session:
        async with session.begin():
            for data in hardcoded_supermarkets:
                supermarket = Supermarket(
                    supermarket_id=data["supermarket_id"],
                    supermarket_name=data["supermarket_name"],
                    location=data["location"]
                )
                session.add(supermarket)
        await session.commit()
        print("Supermarkets table populated.")
    
async def populate_products():
    async with LocalSession() as session:
        async with session.begin():
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

async def populate_orders():
    async with LocalSession() as session:
        async with session.begin():
            for order_data in hardcoded_orders:
                order = Order(
                    id=order_data["id"],
                    customer_name=order_data["customer_name"],
                    total_amount=order_data["total_amount"]
                )
                session.add(order)
                for item_data in order_data["items"]:
                    order_item = OrderItem(
                        id=item_data["id"],
                        order_id=order_data["id"],
                        product_name=item_data["product_name"],
                        quantity=item_data["quantity"],
                        price=item_data["price"]
                    )
                    session.add(order_item)
        await session.commit()
        print("Orders and OrderItems tables populated.")

async def populate_all():
    print("Populating all tables with hardcoded data...")
    await populate_supermarkets()
    await populate_products()
    await populate_users()
    await populate_accommodations()
    await populate_orders()
    print("All tables populated successfully.")

async def main():
    await setDataBase()
    await populate_all()