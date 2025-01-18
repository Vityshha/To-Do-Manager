from app.database import async_session_maker
from app.dao.base import BaseDAO
from sqlalchemy import select

from app.tasks.models import Descriptions


class DescriptionsDAO(BaseDAO):
    model = Descriptions
