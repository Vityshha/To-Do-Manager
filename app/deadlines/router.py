from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.deadlines.models import Deadlines

router = APIRouter(
    prefix='/deadlines',
    tags=['deadlines'],
)


# По конкретному id
# 1. Записать сроки заказа
# 2. Получить сроки заказа
# 3. Изменить сроки заказа


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Deadlines)
        result = await session.execute(query)
        return result.scalars().all()

