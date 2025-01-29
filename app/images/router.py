from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.images.models import Images

router = APIRouter(
    prefix='/images',
    tags=['Images'],
)

