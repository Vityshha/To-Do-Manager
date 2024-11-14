from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.reviews.models import Reviews

router = APIRouter(
    prefix='/reviews',
    tags=['Review'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Reviews)
        result = await session.execute(query)
        return result.scalars().all()

