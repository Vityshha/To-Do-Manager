from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.deadlines.models import Deadlines

router = APIRouter(
    prefix='/deadlines',
    tags=['deadlines'],
)


@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(Deadlines)
        result = await session.execute(query)
        return result.scalars().all()

