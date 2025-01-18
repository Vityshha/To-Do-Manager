from fastapi import APIRouter

from app.tasks.dao import TasksDAO
from app.tasks.schemas import STasks

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)



@router.get('')
async def get_descriptions() -> list[STasks]:
    results = await TasksDAO.find_all()
    return results

