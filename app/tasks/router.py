from fastapi import APIRouter, HTTPException, status
from app.tasks.dao import TasksDAO
from app.tasks.schemas import STasks, STaskCreate, STaskUpdate

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)


@router.post('/', response_model=STasks, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: STaskCreate):
    task = await TasksDAO.add(**task_data.dict())
    return task


@router.get('/', response_model=list[STasks])
async def get_all_tasks():
    tasks = await TasksDAO.find_all()
    return tasks


@router.get('/{task_id}', response_model=STasks)
async def get_task(task_id: int):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")
    return task


@router.put('/{task_id}', response_model=STasks)
async def update_task(task_id: int, task_data: STaskUpdate):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")
    updated_task = await TasksDAO.update(task_id, **task_data.dict(exclude_unset=True))
    return updated_task


@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")
    await TasksDAO.delete(task_id)
    return {"detail": "Task successfully deleted."}
