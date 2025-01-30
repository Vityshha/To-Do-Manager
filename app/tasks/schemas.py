from pydantic import BaseModel
from app.enums import TasksStatus
from datetime import date, datetime
from typing import Optional


class STasks(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TasksStatus
    deadline: Optional[date] = None
    created_at: Optional[date] = None
    column_id: int
    position: int

    class Config:
        from_attributes = True


class STaskCreate(BaseModel):
    title: str
    description: Optional[str]
    status: TasksStatus
    deadline: Optional[date] = None
    column_id: int
    position: int


class STaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TasksStatus]
    deadline: Optional[date]
    column_id: Optional[int]
    position: Optional[int]
