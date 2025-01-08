from pydantic import BaseModel
from fastapi import UploadFile




class DeleteClients(BaseModel):
    """Model for bulk delete"""
    ids: list[int]


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



