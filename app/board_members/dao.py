from app.dao.base import BaseDAO
from app.board_members.models import BoardMembers
from sqlalchemy import select
from app.database import async_session_maker


class BoardMembersDAO(BaseDAO):
    model = BoardMembers

    @classmethod
    async def find_by_user_and_board(cls, user_id: int, board_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id=user_id, board_id=board_id)
            result = await session.execute(query)
            return result.scalars().first()

    @classmethod
    async def find_all_by_board(cls, board_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(board_id=board_id)
            result = await session.execute(query)
            return result.scalars().all()
