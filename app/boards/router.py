from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.boards.models import Boards

router = APIRouter(
    prefix='/boards',
    tags=['Boards'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Boards)
        result = await session.execute(query)
        return result.scalars().all()

