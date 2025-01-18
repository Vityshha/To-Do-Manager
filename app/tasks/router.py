from fastapi import APIRouter

from app.tasks.dao import DescriptionsDAO
from app.tasks.schemas import STasks

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)



@router.get('')
async def get_descriptions() -> list[STasks]:
    results = await DescriptionsDAO.find_all()
    return results

