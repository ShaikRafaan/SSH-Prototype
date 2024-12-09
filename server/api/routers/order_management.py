from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from server.models.order_management import Order, OrderItem
from server.schemas.order_management import OrderCreate, OrderResponse, OrderItemResponse ,OrderUpdate
from server.dependencies import f_database_session
from sqlalchemy.future import select

router = APIRouter()

@router.post("/create", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(f_database_session)):
    new_order = Order(customer_name=order.customer_name, total_amount=order.total_amount)
    db.add(new_order)

    for item in order.items:
        order_item = OrderItem(order_id=new_order.id, product_name=item.product_name, quantity=item.quantity, price=item.price)
        db.add(order_item)

    await db.commit()
    await db.refresh(new_order)

    return new_order
'''
   test
   return OrderResponse(
       id="123",
       customer_name ="John",
       total_amount= "100.4",
       items=[
           OrderItemResponse(
                   product_name="Water",
                   quantity="1",
                   price="50.2",
           ),
           OrderItemResponse(
                   product_name="Milk",
                   quantity="1",
                   price="50.2",
           )
       ]

    )'''

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: AsyncSession = Depends(f_database_session)):

    order = await db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
'''
    Test
      return OrderResponse(
             id="123",
       customer_name ="John",
       total_amount= "100.4",
       items=[
           OrderItemResponse(
                   product_name="Water",
                   quantity="1",
                   price="50.2",
           ),
           OrderItemResponse(
                   product_name="Milk",
                   quantity="1",
                   price="50.2",
           )
       ]

      
   )'''

@router.get("/list", response_model=List[OrderResponse])
async def list_orders(db: AsyncSession = Depends(f_database_session)):

   result = await db.execute(select(Order))
   orders = result.scalars().all()
   return orders
'''
   TEST
     return OrderResponse(
              id="123",
       customer_name ="John",
       total_amount= "100.4",
       items=[
           OrderItemResponse(
                   product_name="Water",
                   quantity="1",
                   price="50.2",
           ),
           OrderItemResponse(
                   product_name="Milk",
                   quantity="1",
                   price="50.2",
           )
       ]

    )'''

@router.put("/update/{order_id}", response_model=OrderResponse)
async def update_order(order_id: int, order_update: OrderUpdate, db: AsyncSession = Depends(f_database_session)):
    stmt = (
        update(Order)
        .where(Order.id == order_id)
        .values(customer_name=order_update.customer_name, total_amount=order_update.total_amount)
        .execution_options(synchronize_session="fetch")
    )
    result = await db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Order not found")

    await db.commit()
    updated_order = await db.get(Order, order_id)
    return updated_order

@router.delete("/delete/{order_id}", response_model=dict)
async def delete_order(order_id: int, db: AsyncSession = Depends(f_database_session)):
    stmt = delete(Order).where(Order.id == order_id)
    result = await db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Order not found")

    await db.commit()
    return {"detail": "Order deleted successfully"}

