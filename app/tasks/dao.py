from app.database import async_session_maker
from app.dao.base import BaseDAO
from sqlalchemy import select
from app.tasks.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def find_by_column(cls, column_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(column_id=column_id)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_by_status(cls, status):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(status=status)
            result = await session.execute(query)
            return result.scalars().all()
