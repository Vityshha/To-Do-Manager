from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SBoards(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class SBoardCreate(BaseModel):
    name: str


class SBoardUpdate(BaseModel):
    name: Optional[str]
