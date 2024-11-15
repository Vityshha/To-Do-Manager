from pydantic import BaseModel
from app.enums import DoorsLoops

class SDescriptions(BaseModel):
    id: int
    doors: int
    loops: DoorsLoops
    platbands: bool
    description: str

    class Config:
        from_attributes = True