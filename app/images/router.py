from fastapi import APIRouter, File, UploadFile, HTTPException
from app.images.dao import ImagesDAO
from uuid import uuid4
from app.config import settings
import os

router = APIRouter(
    prefix='/images',
    tags=['Images'],
)

@router.post('/upload')
async def upload_image(file: UploadFile = File(...)):
    extension = file.filename.split('.')[-1]
    filename = f"{uuid4().hex}.{extension}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    image_data = {"path": filepath}
    await ImagesDAO.add(**image_data)

    return {"filename": filename, "path": filepath}

@router.get('/{image_id}')
async def get_image(image_id: int):
    image = await ImagesDAO.find_by_id(image_id)

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return {"image_id": image.id, "path": image.path}

@router.put('/{image_id}/update')
async def update_image(image_id: int, file: UploadFile = File(...)):
    extension = file.filename.split('.')[-1]
    filename = f"{uuid4().hex}.{extension}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    image_data = {"path": filepath}
    updated_image = await ImagesDAO.update(image_id, **image_data)

    if updated_image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return {"filename": filename, "path": filepath}

@router.delete('/{image_id}/delete')
async def delete_image(image_id: int):
    deleted_image = await ImagesDAO.delete(image_id)

    if deleted_image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return {"detail": "Image successfully deleted"}


