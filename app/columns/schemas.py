from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SColumns(BaseModel):
    id: int
    name: str
    board_id: int
    position: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class SColumnCreate(BaseModel):
    name: str
    board_id: int
    position: int


class SColumnUpdate(BaseModel):
    name: Optional[str]
    position: Optional[int]
