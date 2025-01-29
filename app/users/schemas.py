from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class SUserLogin(BaseModel):
    email: EmailStr
    hashed_password: str
    created_at: date = date.today()
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    image_id: Optional[int] = None

    class Config:
        from_attributes = True


class SUserRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    image_id: Optional[int] = None