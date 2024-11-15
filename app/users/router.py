from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.users.models import Users

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

# 1. Создать юзера
# 2. Удалить юзера
# 3. Отредактировать юзера
# 4. Поставить аватарку
# 5. Как то прописать логику ролей
# 6. Хэшировать пароль
# 7. У юзера должна быть история заказов (воркер он или клиент)
# 8. ...


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Users)
        result = await session.execute(query)
        return result.scalars().all()

