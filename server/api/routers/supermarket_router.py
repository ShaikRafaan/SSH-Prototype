from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models import Supermarket as SupermarketModel
from server.schemas import Supermarket
from server.dependencies import get_db
from server.logging_config import setup_logging  
from typing import List
from sqlalchemy import delete

logger = setup_logging()

router = APIRouter()

@router.get("/list", response_model=List[Supermarket])
async def list_supermarkets(db: AsyncSession = Depends(get_db)) -> List[Supermarket]:
    logger.info("Fetching the list of supermarkets...")
    result = await db.execute(select(SupermarketModel))
    supermarkets = result.scalars().all()
    supermarket_list=[
        Supermarket(
            id=s.supermarket_id,
            name=s.supermarket_name,
            location=s.location
        )
        for s in supermarkets
    ]
    return supermarket_list

@router.post("/add", response_model=Supermarket)
async def add_supermarket(supermarket: Supermarket, db: AsyncSession = Depends(get_db)) -> Supermarket:
    result = await db.execute(select(SupermarketModel).filter_by(id=supermarket.id))
    existing_supermarket = result.scalars().first()
    if existing_supermarket:
        raise HTTPException(
            status_code=400,
            detail=f"A supermarket with id '{supermarket.id}' already exists."
        )
    new_supermarket = SupermarketModel(
        supermarket_id=supermarket.id,
        supermarket_name=supermarket.name,
        location=supermarket.location
    )
    db.add(new_supermarket)
    logger.info(f"Adding a new supermarket with ID: {supermarket.id} and Name: {supermarket.name}")
    await db.commit()
    await db.refresh(new_supermarket) 
    return Supermarket(
        id=new_supermarket.supermarket_id,
        name=new_supermarket.supermarket_name,
        location=new_supermarket.location
    )

@router.get("/search/{id}", response_model=Supermarket)
async def search_products(id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Searching for supermarket with ID: {id}")
    query = select(SupermarketModel).where(SupermarketModel.supermarket_id == id)
    result = await db.execute(query)
    query_result = result.scalar_one_or_none()
    if not query_result:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{id}' not found.")
    return Supermarket(
        id=query_result.supermarket_id,
        name=query_result.supermarket_name,
        location=query_result.location
    )


@router.delete("/delete/{supermarket_id}", response_model=dict)
async def delete_supermarket(supermarket_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    logger.info(f"Attempting to delete supermarket with ID: {supermarket_id}")
    result = await db.execute(
        select(SupermarketModel).where(SupermarketModel.supermarket_id == supermarket_id)
    )
    supermarket = result.scalar_one_or_none()
    if not supermarket:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{supermarket_id}' not found.")
    await db.delete(supermarket)
    await db.commit()
    return {"message": f"Supermarket with ID '{supermarket_id}' has been deleted successfully!"}

@router.put("/update/{supermarket_id}", response_model=Supermarket)
async def update_supermarket(
    supermarket_id: int, 
    updated_data: Supermarket, 
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(SupermarketModel).where(SupermarketModel.supermarket_id == supermarket_id)
    )
    supermarket = result.scalar_one_or_none()

    if not supermarket:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{supermarket_id}' not found.")

    supermarket.supermarket_name = updated_data.name
    supermarket.location = updated_data.location
    await db.commit()
    logger.info(f"Supermarket with ID {supermarket_id} updated successfully.")
    await db.refresh(supermarket)
    return Supermarket(
        id=supermarket.supermarket_id,
        name=supermarket.supermarket_name,
        location=supermarket.location
    )
