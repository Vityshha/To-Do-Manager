from fastapi import APIRouter

from app.descriptions.service import DescriptionsService

router = APIRouter(
    prefix='/descriptions',
    tags=['Описание заказа'],
)

# По конкретному id
# 1. Записать описание заказа
# 2. Получить описание заказа
# 3. Изменить описание заказа


@router.get('')
async def get_descriptions():
    results = await DescriptionsService.find_all()
    return results

