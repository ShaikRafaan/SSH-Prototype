from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.schemas.accommodations import AccommodationUpdate, AccommodationResponse
from server.models.accommodations import Accommodation
from server.dependencies import f_database_session

router = APIRouter(prefix="/accommodations", tags=["Accommodations"])

@router.post("/", response_model=AccommodationResponse)
async def create_accommodation(
    accommodation: AccommodationResponse, db: AsyncSession = Depends(f_database_session)
):
    new_accommodation = Accommodation(**accommodation.dict())
    db.add(new_accommodation)
    await db.commit()
    await db.refresh(new_accommodation)
    return new_accommodation
    """return AccommodationResponse(
        id="1234",
        name= "John",
        address="Myriad"
    )"""

@router.get("/{accommodation_id}", response_model=AccommodationResponse)
async def get_accommodation(
    accommodation_id: int, db: AsyncSession = Depends(f_database_session)
):
    result = await db.execute(select(Accommodation).where(Accommodation.id == accommodation_id))
    accommodation = result.scalars().first()
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation
    """return AccommodationResponse(
        id ="1234",
        name= "John",
        address="Myriad"
    )"""

@router.get("/", response_model=list[AccommodationResponse])
async def list_accommodations(db: AsyncSession = Depends(f_database_session)):
   result = await db.execute(select(Accommodation))
   accommodations = result.scalars().all()
   return accommodations
   """return AccommodationResponse(
       id="1234",
       name="John",
       address="Myriad"
   )"""

@router.put("/{accommodation_id}", response_model=AccommodationResponse)
async def update_accommodation(
    accommodation_id: int, 
    updated_data: AccommodationUpdate, 
    db: AsyncSession = Depends(f_database_session),
):
    result = await db.execute(select(Accommodation).where(Accommodation.id == accommodation_id))
    accommodation = result.scalars().first()
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")

    for field, value in updated_data.dict(exclude_unset=True).items():
        setattr(accommodation, field, value)
    
    db.add(accommodation)
    await db.commit()
    await db.refresh(accommodation)
    return accommodation
    """return AccommodationResponse(
        id="1234",
        name="John",
        address="Myriad"
    )"""

@router.delete("/{accommodation_id}", response_model=dict)
async def delete_accommodation(
    accommodation_id: int, db: AsyncSession = Depends(f_database_session)
):
    result = await db.execute(select(Accommodation).where(Accommodation.id == accommodation_id))
    accommodation = result.scalars().first()
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")

    await db.delete(accommodation)
    await db.commit()
    return {"detail": "Accommodation deleted successfully"}
