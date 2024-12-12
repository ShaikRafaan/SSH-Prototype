from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models import Supermarket as SupermarketModel
from server.schemas import Supermarket
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=List[Supermarket])
async def list_supermarkets(db: AsyncSession = Depends(get_db)) -> List[Supermarket]:
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
    await db.commit()
    await db.refresh(new_supermarket) 
    return Supermarket(
        id=new_supermarket.supermarket_id,
        name=new_supermarket.supermarket_name,
        location=new_supermarket.location
    )
    '''
    new_supermarket = Supermarket(
        name=supermarket.name,
        id=supermarket.id,
        location=supermarket.location
    )
    db.add(new_supermarket)
    await db.commit()
    await db.refresh(new_supermarket)
    return new_supermarket
    '''


@router.get("/search/{id}", response_model=Supermarket)
async def search_products(id: int, db: AsyncSession = Depends(get_db)):
    '''
    query_result = await db.get(SupermarketModel,id)
    
    if not query_result:
        raise HTTPException(status_code=404, detail=f"User with ID '{id}' not found.")
    
    return Supermarket(
            id=query_result.supermarket_id,
            name=query_result.supermarket_name,
            location=query_result.location
        )
    '''
    query = select(SupermarketModel).where(SupermarketModel.supermarket_id == id)
    result = await db.execute(query)
    query_result = result.scalar_one_or_none()

    # If no result is found, raise an HTTP 404 error
    if not query_result:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{id}' not found.")

    # Return the result mapped to the Pydantic model
    return Supermarket(
        id=query_result.supermarket_id,
        name=query_result.supermarket_name,
        location=query_result.location
    )


@router.delete("/delete/{supermarket_id}", response_model=dict)
async def delete_supermarket(supermarket_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    '''
    result = await db.execute(
        select(SupermarketModel).where(Supermarket.id == supermarket_id)
    )
    supermarket = result.scalar_one_or_none()

    if not supermarket:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{id}' not found.")

    await db.delete(supermarket)
    await db.commit()

    return {"message": f"Supermarket with ID {supermarket_id} has been deleted."}
    '''
    '''
    query_result = await db.get(SupermarketModel, supermarket_id)

    if not query_result:
        raise HTTPException(status_code=404, detail=f"User ID '{supermarket_id}' not found.")

    await db.execute(delete(SupermarketModel).filter(SupermarketModel.supermarket_id == supermarket_id))
    await db.commit()

    return {"message":f"User with ID '{supermarket_id}'deleted from database successfully!"}
    '''
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
    await db.refresh(supermarket)
    return Supermarket(
        id=supermarket.supermarket_id,
        name=supermarket.supermarket_name,
        location=supermarket.location
    )
