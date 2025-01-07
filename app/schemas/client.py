from pydantic import BaseModel
from fastapi import Form, UploadFile, File
from typing import Optional

class ClientForm(BaseModel):
    id: int
    full_name: str
    phone: str
    gender: str
    birth_date: str
    address: str
    email: str
    contract_number: str
    contract_type: str
    start_date: str
    group: str
    sport_rank: str
    photo: UploadFile



# Model for bulk delete
class DeleteClientsRequest(BaseModel):
    ids: list[int]