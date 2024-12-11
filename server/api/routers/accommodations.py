from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.accommodations import Accommodation
from server.schemas.accommodations import AccommodationResponse as AccommodationSchema
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=AccommodationSchema)
async def list_accommodations() -> AccommodationSchema:    
    return AccommodationSchema(
        id= "12345",
        address="1725 Slough Avenue"
    )

@router.post("/add", response_model=AccommodationSchema)

async def add_accommodation(accommodation: AccommodationSchema, db: AsyncSession = Depends(get_db)) -> AccommodationSchema:

    return AccommodationSchema(
        id="new-id",
        address="Added accommodation"
    )


@router.get("/search/{id}", response_model=list[AccommodationSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):

    if id == "12345":
        return [AccommodationSchema(id="12345", address="1725 Slough Avenue")]
    else:
        return []

@router.delete("/delete/{accommodation_id}", response_model=dict)
async def delete_accommodation(accommodation_id: str, db: AsyncSession = Depends(get_db)) -> dict:

    if accommodation_id == "12345":
        return {"message": f"accommodation with ID {accommodation_id} has been deleted."}
    else:
        return {"message": f"accommodation with ID {accommodation_id} does not exist."}


@router.put("/update/{accommodation_id}", response_model=AccommodationSchema)
async def update_accommodation(
    accommodation_id: int,update_data: AccommodationSchema,db: AsyncSession = Depends(get_db)) -> AccommodationSchema:

    if accommodation_id == 12345:
        return AccommodationSchema(
            id="12345",
            address=update_data.address or "Updated 1725 Slough Avenue"
        )
    else:
        return AccommodationSchema(
            id=str(accommodation_id),
            address="Non-existent accommodation (for testing purposes)"
        )
