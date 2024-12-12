from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.schemas.accommodations import AccommodationUpdate, AccommodationResponse,AccommodationCreate
from server.models.accommodations import Accommodation
from server.dependencies import get_db

router = APIRouter()
@router.post("/add", response_model=AccommodationResponse)
async def add_supermarket(supermarket: AccommodationResponse, db: AsyncSession = Depends(get_db)) -> AccommodationResponse:
    result = await db.execute(select(Accommodation).filter_by(id=supermarket.id))
    existing_supermarket = result.scalars().first()
    if existing_supermarket:
        raise HTTPException(
            status_code=400,
            detail=f"A supermarket with id '{AccommodationResponse.id}' already exists."
        )
    new_Accommodation = AccommodationResponse(
        id=Accommodation.accommodation_id,
        address=Accommodation.address,
        city=Accommodation.city,
        contact_number=Accommodation.contact_number
    )
    db.add(new_Accommodation)
    await db.commit()
    await db.refresh(new_Accommodation) 
    return AccommodationResponse(
        id=Accommodation.accommodation_id,
        city=Accommodation.city,
        address=Accommodation.address,
        contact_number=Accommodation.contact_number
    )


@router.get("/search/{accommodation_id}", response_model=AccommodationResponse)
async def search_products(id: int, db: AsyncSession = Depends(get_db)):
    query = select(Accommodation).where(Accommodation.accommodation_id == id)
    result = await db.execute(query)
    query_result = result.scalar_one_or_none()
    if not query_result:
        raise HTTPException(status_code=404, detail=f"Accommdations with ID '{id}' not found.")
    return AccommodationResponse(
        id=query_result.accommodation_id,
        city=query_result.city,
        address=query_result.address,
        contact_number=query_result.contact_number
    )

@router.get("/list", response_model=list[AccommodationResponse])
async def list_supermarkets(db: AsyncSession = Depends(get_db)) -> List[AccommodationResponse]:
    result = await db.execute(select(Accommodation))
    Acc = result.scalars().all()
    Accommodation_list=[
        AccommodationResponse(
            id=s.accommodation_id,
            city=s.city,
            address=s.address,
            contact_number=s.contact_number
        )
        for s in Acc
    ]
    return Accommodation_list

@router.put("/update/{accommodation_id}", response_model=AccommodationResponse)
async def update_accommodation(
    accommodation_id: int, 
    updated_data: AccommodationUpdate, 
    db: AsyncSession = Depends(get_db),
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

@router.delete("/delete/{accommodation_id}", response_model=dict)
async def delete_accommodation(
    accommodation_id: int, db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Accommodation).where(Accommodation.id == accommodation_id))
    accommodation = result.scalars().first()
    if not accommodation:
        raise HTTPException(status_code=404, detail="Accommodation not found")

    await db.delete(accommodation)
    await db.commit()
    return {"detail": "Accommodation deleted successfully"}
