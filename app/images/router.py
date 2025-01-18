from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.images.models import Images

router = APIRouter(
    prefix='/images',
    tags=['Images'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Images)
        result = await session.execute(query)
        return result.scalars().all()

