from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.product import Product
from server.schemas.product_schema import Product as ProductSchema
from server.dependencies import get_db
from typing import List

router = APIRouter()

@router.get("/list", response_model=ProductSchema)
async def list_products()->ProductSchema:
    return ProductSchema(
        id=12343,
        name="poptart",
        price=89
    )
'''
@router.get("/search", response_model=list[ProductSchema])
async def search_products(query: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.name.ilike(f"%{query}%")))
    return result.scalars().all()
'''
hardcoded_products = [
    {"id": 1, "name": "iphone", "price": 999},
    {"id": 2, "name": "Samsung Galaxy S21", "price": 799},
    {"id": 3, "name": "Google Pixel 6", "price": 599},
    {"id": 4, "name": "OnePlus 9 Pro", "price": 1069},
    {"id": 5, "name": "Apple MacBook Pro 16", "price": 2399},
]
@router.get("/search/{id}", response_model=ProductSchema)
async def search_products(id: int) -> ProductSchema:
    # Search for the product by id in the hardcoded list
    #product = next((product for product in products if product["id"] == id), None)
    hardcoded_products = [
    {"id": 1, "name": "iphone", "price": 999},
    {"id": 2, "name": "Samsung Galaxy S21", "price": 799},
    {"id": 3, "name": "Google Pixel 6", "price": 599},
    {"id": 4, "name": "OnePlus 9 Pro", "price": 1069},
    {"id": 5, "name": "Apple MacBook Pro 16", "price": 2399},
    ]
    flag = False
    return_product = {}
    count = 0
    for product in hardcoded_products:
        if product["id"] == id:
            flag = True
            return_product = hardcoded_products[count]
        else:
            count += 1
    
    if flag:
        return ProductSchema(
            id=return_product["id"],
            name=return_product["name"],
            price=return_product["price"]
        )
    else:
        return ProductSchema(
            id = 0000,
            name = "null - product not found",
            price=0000
        )