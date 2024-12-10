from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.supermarket import Supermarket
from server.schemas.supermarket_schema import Supermarket as SupermarketSchema
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=SupermarketSchema)
#async def list_supermarkets(db: AsyncSession = Depends(get_db)) -> SupermarketSchema:
async def list_supermarkets() -> SupermarketSchema:    
    #result = await db.execute(select(Supermarket))
    #return result.scalars().all()
    return SupermarketSchema(
        id="12345",
        name="Tomato Sauce"
    )

@router.post("/add", response_model=SupermarketSchema)
#async def search_products(query: str, db: AsyncSession = Depends(get_db)):
async def add_supermarket(supermarket: SupermarketSchema, db: AsyncSession = Depends(get_db)) -> SupermarketSchema:
    '''
    new_supermarket = Supermarket(
        name=supermarket.name,
        id=supermarket.id,
    )
    db.add(new_supermarket)
    await db.commit()
    await db.refresh(new_supermarket)
    return new_supermarket
    '''
    return SupermarketSchema(
        id="new-id",
        name="Added Supermarket"
    )


@router.get("/search/{id}", response_model=list[SupermarketSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):
    '''
    query = select(Supermarket).where(Supermarket.id == id)
    result = await db.execute(query)
    supermarket = result.scalar_one_or_none()

    if not supermarket:
        raise LookupError("Supermarket not found")
    return SupermarketSchema.from_orm(supermarket)
    '''
    if id == "12345":
        return [SupermarketSchema(id="12345", name="Tomato Sauce")]
    else:
        return []

@router.delete("/delete/{supermarket_id}", response_model=dict)
async def delete_supermarket(supermarket_id: str, db: AsyncSession = Depends(get_db)) -> dict:
    '''
    result = await db.execute(
        select(Supermarket).where(Supermarket.id == supermarket_id)
    )
    supermarket = result.scalar_one_or_none()

    if not supermarket:
        raise LookupError("Supermarket not found")

    await db.delete(supermarket)
    await db.commit()

    return {"message": f"Supermarket with ID {supermarket_id} has been deleted."}
    '''
    if supermarket_id == "12345":
        return {"message": f"Supermarket with ID {supermarket_id} has been deleted."}
    else:
        return {"message": f"Supermarket with ID {supermarket_id} does not exist."}


@router.put("/update/{supermarket_id}", response_model=SupermarketSchema)
async def update_supermarket(
    supermarket_id: int,update_data: SupermarketSchema,db: AsyncSession = Depends(get_db)) -> SupermarketSchema:
    '''
    result = await db.execute(select(Supermarket).where(Supermarket.id == supermarket_id))
    supermarket = result.scalar_one_or_none()

    if not supermarket:
        raise LookupError("Supermarket not found")

    # Update fields
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(supermarket, key, value)

    await db.commit()
    await db.refresh(supermarket)

    return supermarket
    '''
    if supermarket_id == 12345:
        return SupermarketSchema(
            id="12345",
            name=update_data.name or "Updated Tomato Sauce"
        )
    else:
        return SupermarketSchema(
            id=str(supermarket_id),
            name="Non-existent supermarket (for testing purposes)"
        )
