from app.dao.base import BaseDAO
from app.boards.models import Boards
from sqlalchemy import select, insert
from app.database import async_session_maker


class BoardsDAO(BaseDAO):
    model = Boards

    @classmethod
    async def find_by_name(cls, name: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(name=name)
            result = await session.execute(query)
            return result.scalars().first()

    @classmethod
    async def add_board(cls, **data):
        async with async_session_maker() as session:
            board = cls.model(**data)
            session.add(board)
            await session.commit()
            await session.refresh(board)
            return board