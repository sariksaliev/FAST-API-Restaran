from fastapi import APIRouter, HTTPException
from database.orderservice import *
from orders import OrderValidator

order_router = APIRouter(prefix='/order', tags=['Для работы с заказами'])

# Создание нового заказа
@order_router.post('/new-order')
async def create_new(dish_id: int, customer_id: int):
    new_order = creation_new_order(dish_id, customer_id)
    return new_order


# Получить все заказы
@order_router.get('/all-order')
async def get_all_orders(customer_id):
    get_order = all_order(customer_id=customer_id)
    if get_order:
        return get_order

@order_router.get("/get-all-orders")
async def gett_all_orders():
    all_orders = gett_all_orders1()
    return all_orders

# Получение информации о конкретном заказе
@order_router.get('/get-order')
async def get_order11(order_id):
    order = get_order_by_id(order_id=order_id)
    return order

# Обновление заказа
@order_router.put('/update-order')
async def update_order_info(order_id: int, dish_id: int, customer_id: int):
    if update_order(order_id, dish_id, customer_id):
        return {'message': 'Информация о заказе успешно обновлена'}
    else:
        raise HTTPException(status_code=404, detail="Заказ не найден")

# Удаление заказа
@order_router.delete('/del-order')
async def delete_order_by_id(order_id: int):
    if delete_order(order_id):
        return {'message': f'Заказ с ID {order_id} успешно удален'}
    else:
        raise HTTPException(status_code=404, detail="Заказ не найден")
