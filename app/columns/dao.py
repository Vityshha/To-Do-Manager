from app.database import async_session_maker
from app.dao.base import BaseDAO
from sqlalchemy import select
from app.columns.models import Columns


class ColumnsDAO(BaseDAO):
    model = Columns

    @classmethod
    async def find_by_board(cls, board_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(board_id=board_id)
            result = await session.execute(query)
            return result.scalars().all()
