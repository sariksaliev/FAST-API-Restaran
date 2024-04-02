from fastapi import APIRouter
from database.customerservice import create_new_customer, update_customer_balance, delete_customer, get_customer_info, get_all_customers
from customer import CustomerValidator


cus_router = APIRouter(prefix='/customer', tags=['Для работы с клиентами'])

# Создаем нового клиента ...
@cus_router.post("/customer/")
async def create_new_customer_1(customer: CustomerValidator):
    new_customer = create_new_customer(**customer)
    if new_customer:
        return {"message": f"Создание клиента {customer} успешно создан"}
    else:
        return {"message": f"Ошибка при создании клиента {customer}"}


# Обновляем баланс клиента
@cus_router.put("/customer/update")
async def update_customer_balance_endpoint(customer_id: int, balance: float):
    # Обновить баланс клиента.
    updated_customer = update_customer_balance(customer_id, balance)
    if updated_customer:
        return {"message": f"Баланс клиента с ID {customer_id} успешно обновлен"}
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Удаляем клиента
@cus_router.delete("/customer/delete")
async def delete_customer_endpoint(customer_id: int):
    # Удалить клиента по его ID.
    deleted_customer = delete_customer(customer_id)
    if deleted_customer:
        return {"message": f"Клиент с ID {customer_id} успешно удален"}
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Получаем информацию о клиенте по его ID
@cus_router.get("/customer/get")
async def get_customer_info_endpoint(customer_id: int):
    # Получить информацию о клиенте по его ID.
    customer = get_customer_info(customer_id)
    if customer:
        return customer
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Получаем список всех клиентов
@cus_router.get("/customers/all")
async def get_all_customers_endpoint():
    # Получить список всех клиентов.
    return get_all_customers()
