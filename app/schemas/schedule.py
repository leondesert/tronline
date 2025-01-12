from pydantic import BaseModel
from typing import List

class DeleteClasses(BaseModel):
    """Model for bulk delete"""
    ids: list[int]


class Schedule(BaseModel):
    id: int
    weekday: int
    coaches: str
    group: int
    start: int
    end: int
    comment: str