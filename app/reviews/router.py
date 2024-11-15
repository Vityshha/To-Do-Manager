from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.reviews.models import Reviews

router = APIRouter(
    prefix='/reviews',
    tags=['Review'],
)


# По конкретному id
# 1. Записать отзыв о заказке
# 2. Получить отзыв о заказе
# 3. Изменить отзыв о заказе
# todo возможно reviews не обязательно, хватит и звездочек

@router.get('')
async def get_reviews():
    async with async_session_maker() as session:
        query = select(Reviews)
        result = await session.execute(query)
        return result.scalars().all()

