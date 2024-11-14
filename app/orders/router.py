from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.orders.models import Orders

router = APIRouter(
    prefix='/orders',
    tags=['Orders'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Orders)
        result = await session.execute(query)
        return result.scalars().all()

