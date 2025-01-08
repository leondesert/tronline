from pydantic import BaseModel
from typing import List



class DeleteGroups(BaseModel):
    """Model for bulk delete"""
    ids: list[int]



class RepeaterGroup(BaseModel):
    schedule: str

class GroupForm(BaseModel):
    name: str
    sport_type: str
    coaches: str
    start_date: str
    position: int
    repeater_group: List[RepeaterGroup]
