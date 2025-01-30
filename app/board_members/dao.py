from app.dao.base import BaseDAO
from app.board_members.models import BoardMembers
from sqlalchemy import select, insert, delete
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

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            member_id = result.scalar()
            return await cls.find_by_id(member_id)

    @classmethod
    async def delete(cls, member_id: int):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == member_id)
            await session.execute(query)
            await session.commit()