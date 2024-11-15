from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.workers.models import Workers

router = APIRouter(
    prefix='/workers',
    tags=['workers'],
)


# По конкретному id
# 1. Создать воркера по user_id
# 2. Получить воркеров по id
# 3. Изменить параметры воркера


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Workers)
        result = await session.execute(query)
        return result.scalars().all()

