from fastapi import APIRouter
from database.dishservice import get_all_dishes, add_new_dish, get_dish_by_id, update_dish_price
from dishes import DishValidator

dish_router = APIRouter(prefix='/dish', tags=['Для работы с блюдами'])


# Получение списка всех блюд
@dish_router.get('/dishes')
async def get_all_dishes():
    all_dishes = get_all_dishes()
    if all_dishes:
        # return {'message': }
    else:
        return {'message': 'Ошибка при получении списка всех блюд'}

# Добавление нового блюда
@dish_router.post('/add-dish')
async def add_new_dish(customer_id: int, dish_name: str, description: str, price: float):
    new_dish = add_new_dish(customer_id=customer_id, dish_name=dish_name, description=description, price=price)
    if new_dish:
        return {'message': 'Блюдо добавлено'}
    else:
        return {'message': 'Ошибка при добавлении блюда'}

# Получение информации о конкретном блюде
@dish_router.get('/get-dish')
async def get_dish_by_id(dish_id: int):
    get_dish = get_dish_by_id(dish_id=dish_id)
    if get_dish:
        return {'message': 'Информация о блюде'}
    else:
        return {'message': 'Ошибка при получении информации о блюде'}


# Обновление информации о блюде
@dish_router.put('/update-dish')
async def update_dish_price(dish_id: int, new_price: float):
    dish_price = update_dish_price(dish_id=dish_id, new_price=new_price)
    if dish_price:
        return {'message': 'Информация о блюде обновлена'}
    else:
        return {'message': 'Ошибка при обновлении информации о блюде'}



# Удаление блюда
@dish_router.delete('/del-dish')
async def delete_dish(dish_id: int):
    del_dish = delete_dish(dish_id=dish_id)
    if del_dish:
        return {'message': 'Блюдо удалено'}
    else:
        return {'message': 'Ошибка при удалении блюда'}