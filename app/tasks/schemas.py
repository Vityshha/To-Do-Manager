from pydantic import BaseModel
from app.enums import TasksStatus
from datetime import datetime

class STasks(BaseModel):
    id: int
    title: str
    description: str
    status: TasksStatus
    deadline: datetime
    created_at: datetime
    column_id: int
    position: int

    class Config:
        from_attributes = True