from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.users.models import Users

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Users)
        result = await session.execute(query)
        return result.scalars().all()

