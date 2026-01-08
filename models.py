from pydantic import BaseModel
class Expense(BaseModel):
    date: str
    category: str
    amount: float
    description: str
    payment_mode: str
    merchant_name: str
    location: str
    notes: str
    created_by: str
