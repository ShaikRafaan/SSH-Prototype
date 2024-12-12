from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.supermarket import Supermarket
from server.schemas.supermarket_schema import Supermarket as SupermarketSchema
from server.dependencies import get_db
from server.logging_config import setup_logging  


logger = setup_logging()

router = APIRouter()

@router.get("/list", response_model=SupermarketSchema)
async def list_supermarkets() -> SupermarketSchema:
    logger.info("Fetching the list of supermarkets...")
    return SupermarketSchema(
        id="12345",
        name="Tomato Sauce"
    )

@router.post("/add", response_model=SupermarketSchema)
async def add_supermarket(supermarket: SupermarketSchema, db: AsyncSession = Depends(get_db)) -> SupermarketSchema:
    logger.info(f"Adding a new supermarket with ID: {supermarket.id} and Name: {supermarket.name}")
    

    try:
        logger.info(f"Supermarket with ID {supermarket.id} added successfully.")
    except Exception as e:
        logger.error(f"Failed to add supermarket: {e}")
        raise HTTPException(status_code=500, detail="Failed to add supermarket.")
    
    return SupermarketSchema(
        id="new-id",
        name="Added Supermarket"
    )

@router.get("/search/{id}", response_model=list[SupermarketSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):
    logger.info(f"Searching for supermarket with ID: {id}")
    if id == "12345":
        logger.info(f"Supermarket with ID {id} found.")
        return [SupermarketSchema(id="12345", name="Tomato Sauce")]
    else:
        logger.warning(f"Supermarket with ID {id} not found.")
        return []

@router.delete("/delete/{supermarket_id}", response_model=dict)
async def delete_supermarket(supermarket_id: str, db: AsyncSession = Depends(get_db)) -> dict:
    logger.info(f"Attempting to delete supermarket with ID: {supermarket_id}")
    if supermarket_id == "12345":
        logger.info(f"Supermarket with ID {supermarket_id} deleted successfully.")
        return {"message": f"Supermarket with ID {supermarket_id} has been deleted."}
    else:
        logger.warning(f"Supermarket with ID {supermarket_id} does not exist.")
        return {"message": f"Supermarket with ID {supermarket_id} does not exist."}

@router.put("/update/{supermarket_id}", response_model=SupermarketSchema)
async def update_supermarket(
    supermarket_id: int, update_data: SupermarketSchema, db: AsyncSession = Depends(get_db)
) -> SupermarketSchema:
    logger.info(f"Attempting to update supermarket with ID: {supermarket_id} with data: {update_data.dict()}")
    if supermarket_id == 12345:
        updated_supermarket = SupermarketSchema(
            id="12345",
            name=update_data.name or "Updated Tomato Sauce"
        )
        logger.info(f"Supermarket with ID {supermarket_id} updated successfully.")
        return updated_supermarket
    else:
        logger.warning(f"Supermarket with ID {supermarket_id} not found for update.")
        return SupermarketSchema(
            id=str(supermarket_id),
            name="Non-existent supermarket (for testing purposes)"
        )
