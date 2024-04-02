from pydantic import BaseModel


# Валидатор для заказов
class DishValidator(BaseModel):
    dish_id: int
    customer_id: int
    dish_name: str
    description: str
    price: float