from pydantic import BaseModel, EmailStr
from datetime import date

# Pydantic модель для проверки входных данных
class Client(BaseModel):
    full_name: str
    phone: str
    gender: str
    birth_date: date
    address: str
    email: EmailStr
    contract_number: str
    contract_type: str
    start_date: date
    group: str
    sport_rank: str
    photo: str
    comment: str | None = None

