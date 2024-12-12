from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.product import Product as ProductModel
from server.schemas.product_schema import Product, ProductCreate
from server.dependencies import get_db
from typing import List

router = APIRouter()

@router.get("/product_list", response_model=List[Product])
async def list_product(db: AsyncSession = Depends(get_db)) -> List[Product]:
    result = await db.execute(select(ProductModel))
    products = result.scalars().all()
    product_list=[
        Product(
            id=s.product_id,
            name=s.product_name,
            price=s.price,
            in_stock=s.in_stock,
            supermarket_id=s.supermarket_id
        )
        for s in products
    ]
    return product_list

@router.get("/search/{id}", response_model=Product)
async def search_products(id: int, db: AsyncSession = Depends(get_db)):
    query = select(ProductModel).where(ProductModel.id == id)
    result = await db.execute(query)
    query_result = result.scalar_one_or_none()
    if not query_result:
        raise HTTPException(status_code=404, detail=f"Product with ID '{id}' not found.")
    return Product(
        id=query_result.supermarket_id,
        product_name=query_result.product_name,
        price=query_result.price,
        in_stock=query_result.in_stock

    )