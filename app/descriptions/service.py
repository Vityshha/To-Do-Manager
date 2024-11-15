from app.database import async_session_maker
from app.dao.base import BaseService
from sqlalchemy import select

from app.descriptions.models import Descriptions


class DescriptionsService(BaseService):
    model = Descriptions
