from app.dao.base import BaseDAO
from app.images.models import Images


class ImagesDAO(BaseDAO):
    model = Images