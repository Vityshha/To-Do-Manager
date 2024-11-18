from pydantic import BaseModel, EmailStr
from datetime import date
from app.enums import RoleUser



class SUserRegister(BaseModel):
    email: EmailStr
    password: str
    role: RoleUser
    date_registration: date
    adress: str
    first_name: str
    last_name: str
    image_id: int