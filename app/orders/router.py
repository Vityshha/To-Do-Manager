from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.orders.models import Orders

router = APIRouter(
    prefix='/orders',
    tags=['Orders'],
)


# 1. Создать заказ
# 2. Отредактировать заказ
# 3. Удалить заказ
# todo воркер не обязательное поле, либо сервер либо менеджер назначить должен
# 4. Получать подходящих по сроку и по опыту воркера
# 5. Назначить воркера на заказ


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Orders)
        result = await session.execute(query)
        return result.scalars().all()

