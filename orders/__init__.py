from pydantic import BaseModel


# Валидатор для заказов
class OrderValidator(BaseModel):
    order_id: int
    dish_id: int
    customer_id: int