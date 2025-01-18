from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.board_members.models import BoardMembers

router = APIRouter(
    prefix='/board_members',
    tags=['Board members'],
)



@router.get('')
async def get_orders():
    async with async_session_maker() as session:
        query = select(BoardMembers)
        result = await session.execute(query)
        return result.scalars().all()

