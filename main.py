from fastapi import FastAPI
from customer.customers_api import cus_router
from dishes.dish_api import dish_router
from orders.order_api import order_router


from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')
app.include_router(order_router)
app.include_router(dish_router)
app.include_router(cus_router)