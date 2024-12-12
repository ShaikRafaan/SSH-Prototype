from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.schemas.accommodations import AccommodationUpdate, AccommodationResponse,AccommodationCreate
from server.models.accommodations import Accommodation
from server.schemas.accommodations import AccommodationResponse as AccommodationSchema
from server.dependencies import get_db

router = APIRouter()
@router.post("/add", response_model=AccommodationResponse)
async def add_accommodation(accommodation: AccommodationResponse, db: AsyncSession = Depends(get_db)) -> AccommodationResponse:
    result = await db.execute(select(Accommodation).filter_by(id=accommodation.id))
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
async def search_accommodation(id: int, db: AsyncSession = Depends(get_db)):
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
async def list_accommodation(db: AsyncSession = Depends(get_db)) -> List[AccommodationResponse]:
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
    acc_id: int, 
    updated_data: AccommodationResponse, 
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Accommodation).where(Accommodation.accommodation_id == acc_id)
    )
    acc = result.scalar_one_or_none()

    if not acc:
        raise HTTPException(status_code=404, detail=f"Accommodation with ID '{acc_id}' not found.")

    AccommodationResponse.address = updated_data.address
    AccommodationResponse.city = updated_data.city
    AccommodationResponse.contact_number=updated_data.contact_number
    await db.commit()
    await db.refresh(acc)
    return acc(
        id=Accommodation.accommodation_id,
        address=Accommodation.address,
        city=Accommodation.city,
        contact_number=Accommodation.contact_number
    )


@router.delete("/delete/{accommodation_id}", response_model=dict)
async def delete_accommodation(accom_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    result = await db.execute(
        select(Accommodation).where(Accommodation.accommodation_id == accom_id)
    )
    acc = result.scalar_one_or_none()
    if not acc:
        raise HTTPException(status_code=404, detail=f"Supermarket with ID '{accom_id}' not found.")
    await db.delete(acc)
    await db.commit()
    return {"message": f"Supermarket with ID '{accom_id}' has been deleted successfully!"}
