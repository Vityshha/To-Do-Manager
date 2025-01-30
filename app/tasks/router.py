from fastapi import APIRouter, HTTPException, status, File, UploadFile
from app.tasks.dao import TasksDAO
from app.images.dao import ImagesDAO
from app.tasks.schemas import STasks, STaskCreate, STaskUpdate
from datetime import date, datetime


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)


@router.post('/', response_model=STasks, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: STaskCreate):
    task_data_dict = task_data.dict()
    task_data_dict['created_at'] = datetime.now()
    task_data_dict['deadline'] = None
    task = await TasksDAO.added_task(**task_data_dict)
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



@router.post('/{task_id}/image')
async def add_image(task_id: int, file: UploadFile = File(...)):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    image = await ImagesDAO.upload_image(file)
    await TasksDAO.update(task_id, image_id=image["image_id"])

    return {"detail": "Image added successfully"}

@router.put('/{task_id}/image')
async def update_image(task_id: int, file: UploadFile = File(...)):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    image = await ImagesDAO.update_image(task.image_id, file)

    await TasksDAO.update(task_id, image_id=image["image_id"])

    return {"detail": "Image updated successfully", "filename": image["filename"], "path": image["path"]}

@router.delete('/{task_id}/image')
async def delete_imsge(task_id: int):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.image_id != 0:
        await ImagesDAO.delete_image(task.image_id)
        #todo нужно ссылаться на таблицу image.id
        await TasksDAO.update(task_id, image_id=None)

    return {"detail": "Image deleted successfully"}