from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from server.models.order_management import Order
from server.schemas.order_management import OrderResponse as OrderSchema
from server.schemas.order_management import OrderItemResponse
from server.dependencies import get_db

router = APIRouter()

@router.get("/list", response_model=OrderSchema)
async def list_order_management() -> OrderSchema:    
    return OrderSchema(
        id="12345",
        customer_name="Alice",
        total_amount= 150.50,
        items= [OrderItemResponse (id= "12345",
                product_name="Laptop",
                quantity= 1,
                price= 150.50
                )]

    )

@router.post("/add", response_model=OrderSchema)
async def add_order(order: OrderSchema, db: AsyncSession = Depends(get_db)) -> OrderSchema:

    return OrderSchema(
        id="12345",
        customer_name="Alice",
        total_amount= 150.50,
        items= [OrderItemResponse (id= "12345",
                product_name="Laptop",
                quantity= 1,
                price= 150.50
                )]
    )

@router.get("/search/{id}", response_model=list[OrderSchema])
async def search_products(id: str, db: AsyncSession = Depends(get_db)):
    if id == "12345":
        return [OrderSchema(id="12345", customer_name="Alice", total_amount=150.50, items=[OrderItemResponse( id= "12345", product_name="Laptop", quantity= 1, price= 150.50)])]
    else:
        return []

@router.delete("/delete/{order_id}", response_model=dict)
async def delete_order(order_id: str, db: AsyncSession = Depends(get_db)) -> dict:

    if order_id == "12345":
        return {"message": f"order with ID {order_id} has been deleted."}
    else:
        return {"message": f"order with ID {order_id} does not exist."}


@router.put("/update/{order_id}", response_model=OrderSchema)
async def update_order(
    order_id: int,update_data: OrderSchema,db: AsyncSession = Depends(get_db)) -> OrderSchema:

    if order_id == 12345:
        return OrderSchema(
            id="12345",
            customer_name="Alice",
            total_amount= 150.50,
            items= [OrderItemResponse (id= "12345", product_name="Laptop", quantity= 1, price= 150.50)]
    )
    else:
        return OrderSchema(
            id=str(order_id),
            customer_name="Non-existent order (for testing purposes)",
            total_amount=0,
            items= [OrderItemResponse (id= "Non-existent order (for testing purposes)", product_name="Non-existent order (for testing purposes)", quantity= 0, price= 0)]
    )
