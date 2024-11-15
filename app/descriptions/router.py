from fastapi import APIRouter

from app.descriptions.dao import DescriptionsDAO
from app.descriptions.schemas import SDescriptions

router = APIRouter(
    prefix='/descriptions',
    tags=['Описание заказа'],
)

# По конкретному id
# 1. Записать описание заказа
# 2. Получить описание заказа
# 3. Изменить описание заказа


@router.get('')
async def get_descriptions() -> list[SDescriptions]:
    results = await DescriptionsDAO.find_all()
    return results

