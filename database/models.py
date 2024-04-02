from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    address = Column(String)
    balance = Column(Float, default=0)

    orders = relationship("Order", lazy='subquery')

class Dish(Base):
    __tablename__ = "dishes"
    dish_id = Column(Integer, primary_key=True, autoincrement=True)
    dish_name = Column(String)
    description = Column(String)
    price = Column(Float)

    orders = relationship("Order", lazy='subquery')

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("dishes.dish_id"))
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))

    dish = relationship("Dish", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")

    # Пример связи между таблицами
    dish = relationship("Dish", lazy='subquery')
    customer = relationship("Customer", lazy='subquery')

