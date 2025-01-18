from pydantic import BaseModel, EmailStr
from datetime import date


class SUserAuth(BaseModel):
    email: EmailStr
    hashed_password: str
    created_at: date
    first_name: str
    last_name: str
    image_id: int