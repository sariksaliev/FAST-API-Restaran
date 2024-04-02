from database import get_db
from database.models import Order


# Добавить заказ
def creation_new_order(dish_id, customer_id):

    db = next(get_db())

    new_order = db.query(Order).filter_by(customer_id=customer_id, dish_id=dish_id).first()

    if new_order:
        db.add(new_order)
        db.commit()
        return 'Заказ успешно создан'
    else:
        return f'Ошибка при создании заказа'



# Удаление заказа
def delete_order(order_id):

    db = next(get_db())

    order = db.query(Order).filter_by(order_id=order_id).first()

    if order:
        db.delete(order)
        db.commit()
        return 'Заказ успешно удален'
    else:
        return f'Ошибка при удалении заказа'


# Получить все заказы
def all_order(customer_id):

    db = next(get_db())

    all_order = db.query(Order).filter_by(customer_id=customer_id).all()
    if all_order:
        return all_order
    else:
        return 'Ошибка при получении заказов клиента'

def gett_all_orders1():
    db = next(get_db())
    all_order = db.query(Order).all()
    if all_order:
        return all_order
    else:
        return 'Ошибка при получении всех заказов'


# Обновления заказа
def update_order(order_id, customer_id, dish_id):

    db = next(get_db())

    order = db.query(Order).filter_by(order_id=order_id).first()

    if order:
        order.customer_id = customer_id
        order.dish_id = dish_id
        try:
            db.commit()
            return 'Заказ успешно обновлен'
        except Exception as e:
            db.rollback()
            return f'Ошибка при обновлении заказа: {str(e)}'
    else:
        return 'Заказ не найден'


# Получение заказа от клиента
def get_order_by_id(order_id):

    db = next(get_db())

    get_order = db.query(Order).filter_by(order_id=order_id).first()

    if get_order:
        return get_order
    else:
        return 'Заказ не найден'