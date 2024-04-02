from pydantic import BaseModel

class CustomerValidator(BaseModel):
    customer_id: int
    name: str
    surname: str
    phone_number: int
    address: str

