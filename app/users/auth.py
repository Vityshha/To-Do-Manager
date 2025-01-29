from datetime import datetime, timedelta
from app.users.dao import UsersDAO
from passlib.context import CryptContext
from pydantic import EmailStr
from jose import jwt
from app.config import settings



pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password: str) -> str:
    return pwd_context.hash((password))

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jtw = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jtw

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.hashed_password):
        return None
    return user
