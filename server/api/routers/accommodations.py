from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.accommodations import Accommodation
from server.schemas.accommodations import AccommodationResponse as AccommodationSchema
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=AccommodationSchema)
#async def list_accommodations(db: AsyncSession = Depends(get_db)) -> AccommodationSchema:
async def list_accommodations() -> AccommodationSchema:    
    #result = await db.execute(select(accommodation))
    #return result.scalars().all()
    return AccommodationSchema(
        id= "12345",
        address="1725 Slough Avenue"
    )

@router.post("/add", response_model=AccommodationSchema)
#async def search_products(query: str, db: AsyncSession = Depends(get_db)):
async def add_accommodation(accommodation: AccommodationSchema, db: AsyncSession = Depends(get_db)) -> AccommodationSchema:
    '''
    new_accommodation = accommodation(
        name=accommodation.name,
        id=accommodation.id,
    )
    db.add(new_accommodation)
    await db.commit()
    await db.refresh(new_accommodation)
    return new_accommodation
    '''
    return AccommodationSchema(
        id="new-id",
        address="Added accommodation"
    )


@router.get("/search/{id}", response_model=list[AccommodationSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):
    '''
    query = select(accommodation).where(accommodation.id == id)
    result = await db.execute(query)
    accommodation = result.scalar_one_or_none()

    if not accommodation:
        raise LookupError("accommodation not found")
    return AccommodationSchema.from_orm(accommodation)
    '''
    if id == "12345":
        return [AccommodationSchema(id="12345", address="1725 Slough Avenue")]
    else:
        return []

@router.delete("/delete/{accommodation_id}", response_model=dict)
async def delete_accommodation(accommodation_id: str, db: AsyncSession = Depends(get_db)) -> dict:
    '''
    result = await db.execute(
        select(accommodation).where(accommodation.id == accommodation_id)
    )
    accommodation = result.scalar_one_or_none()

    if not accommodation:
        raise LookupError("accommodation not found")

    await db.delete(accommodation)
    await db.commit()

    return {"message": f"accommodation with ID {accommodation_id} has been deleted."}
    '''
    if accommodation_id == "12345":
        return {"message": f"accommodation with ID {accommodation_id} has been deleted."}
    else:
        return {"message": f"accommodation with ID {accommodation_id} does not exist."}


@router.put("/update/{accommodation_id}", response_model=AccommodationSchema)
async def update_accommodation(
    accommodation_id: int,update_data: AccommodationSchema,db: AsyncSession = Depends(get_db)) -> AccommodationSchema:
    '''
    result = await db.execute(select(accommodation).where(accommodation.id == accommodation_id))
    accommodation = result.scalar_one_or_none()

    if not accommodation:
        raise LookupError("accommodation not found")

    # Update fields
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(accommodation, key, value)

    await db.commit()
    await db.refresh(accommodation)

    return accommodation
    '''
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
