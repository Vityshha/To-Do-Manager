from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.columns.models import Columns

router = APIRouter(
    prefix='/columns',
    tags=['Columns'],
)


@router.get('')
async def get_reviews():
    async with async_session_maker() as session:
        query = select(Columns)
        result = await session.execute(query)
        return result.scalars().all()

