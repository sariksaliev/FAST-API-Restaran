from database import get_db
from datetime import datetime
from database.models import Customer


# Создаем клиента
def create_new_customer(name: str, surname: str, phone_number: int, address: str):
    db = next(get_db())
    customer = db.query(Customer).filter_by(name=name, surname=surname, phone_number=phone_number,
                                            address=address).first()

    if customer:
        db.add(customer)
        db.commit()

        return 'Клиент успешно создан'
    else:
        return 'Не получилось создать клиента'


# Обновляем баланс клиента
def update_customer_balance(customer_id: int, new_balance: float):
    db = next(get_db())
    customer = db.query(Customer).filter_by(customer_id=customer_id).first()
    if customer:
        customer.balance = new_balance
        db.commit()
        return 'Баланс клиента обновлен'
    else:
        return 'Не получилось обновить баланс клиента'


# Удаляем клиента
def delete_customer(customer_id: int):
    db = next(get_db())
    customer = db.query(Customer).filter_by(customer_id=customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
        return 'Клиент успешно удален'
    else:
        return 'Не получилось удалить клиента'


# Получаем информацию о клиенте по его ID
def get_customer_info(customer_id: int):
    db = next(get_db())
    customer = db.query(Customer).filter_by(customer_id=customer_id).first()
    if customer:
        return f"Имя: {customer.name}\nФамилия: {customer.surname}\nНомер телефона: {customer.phone_number}\nАдрес: {customer.address}\nБаланс: {customer.balance}"
    else:
        return 'Клиент не найден'


# Получаем список всех клиентов
def get_all_customers():
    db = next(get_db())
    customers = db.query(Customer).all()
    if customers:
        customer_list = ""
        for customer in customers:
            customer_list += f"ID: {customer.customer_id}, Имя: {customer.name}, Фамилия: {customer.surname}\n"
        return customer_list
    else:
        return 'Список клиентов пуст'
