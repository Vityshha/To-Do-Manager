from app.dao.base import BaseDAO
from app.boards.models import Boards
from sqlalchemy import select
from app.database import async_session_maker


class BoardsDAO(BaseDAO):
    model = Boards

    @classmethod
    async def find_by_name(cls, name: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(name=name)
            result = await session.execute(query)
            return result.scalars().first()
