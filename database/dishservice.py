from database.models import Dish
from database import get_db



# Получение списка всех блюд
def get_all_dishes():
    try:
        db = next(get_db())
        all_dish = db.query(Dish).all()
        return all_dish
    except Exception as e:
        # Обработка ошибок, например, логирование и возврат сообщения об ошибке
        return []

# Добавление нового блюдо Dish
def add_new_dish(customer_id, dish_name, description, price):
    db = next(get_db())

    # Проверяем, существует ли уже такое блюдо
    dish = db.query(Dish).filter_by(customer_id=customer_id, dish_name=dish_name, description=description,
                                    price=price).first()

    # Если блюдо не существует, добавляем его в базу данных
    if not dish:
        new_dish = Dish(customer_id=customer_id, dish_name=dish_name, description=description, price=price)
        db.add(new_dish)
        db.commit()
        return 'Блюдо добавлено'
    else:
        return 'Блюдо уже существует'


#  Получения объекта блюдо по идентификатору
def get_dish_by_id(dish_id):
    db = next(get_db())
    dish = db.query(Dish).filter_by(dish_id=dish_id).first()
    if dish:
        return 'Получено успешно'
    else:
        return 'Ошибка: блюдо не найдено'

# Обновления цены блюдо
def update_dish_price(dish_id, new_price):
    db = next(get_db())
    dish = db.query(Dish).filter_by(dish_id=dish_id).first()
    if dish:
        dish.price = new_price
        db.commit()
        return 'Цена блюда успешно обновлена'
    else:
        return 'Тополмадик'


# Метод для удаления блюдо
def delete_dish(dish_id):
    db = next(get_db())
    dish = db.query(Dish).filter_by(dish_id=dish_id).first()
    if dish:
        db.delete(dish)
        db.commit()
        return 'Блюдо к сожалению удалено'
    else:
        return 'Блюдо не найдено'
