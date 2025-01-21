from pydantic import BaseModel, EmailStr
from datetime import date


class SUserAuth(BaseModel):
    email: EmailStr
    hashed_password: str
    created_at: date
    first_name: str
    last_name: str
    image_id: int

    class Config:
        from_attributes = True


class SUserCreate(BaseModel):
    email: EmailStr
    password: str  # Пароль без хэширования
    first_name: str
    last_name: str
    image_id: int


class SUserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: date
    first_name: str
    last_name: str
    image_id: int

    class Config:
        from_attributes = True
