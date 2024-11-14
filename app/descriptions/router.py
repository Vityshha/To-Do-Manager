from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.descriptions.models import Descriptions

router = APIRouter(
    prefix='/descriptions',
    tags=['descriptions'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Descriptions)
        result = await session.execute(query)
        return result.scalars().all()

