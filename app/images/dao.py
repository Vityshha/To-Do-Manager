from fastapi import HTTPException, File, UploadFile
from app.dao.base import BaseDAO
from app.images.models import Images
from uuid import uuid4
from app.config import settings
import os

class ImagesDAO(BaseDAO):
    model = Images

    @classmethod
    async def upload_image(cls, file: UploadFile = File(...)):
        extension = file.filename.split('.')[-1]
        filename = f"{uuid4().hex}.{extension}"
        filepath = os.path.join(settings.UPLOAD_DIR, filename)

        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())
        image_data = {"path": filepath}
        return await cls.add_image(**image_data)

    @classmethod
    async def update_image(cls, image_id: int, file: UploadFile = File(...)):
        image = await cls.find_by_id(image_id)

        if not image:
            raise HTTPException(status_code=404, detail="Image not found")

        extension = file.filename.split('.')[-1]
        filename = f"{uuid4().hex}.{extension}"
        filepath = os.path.join(settings.UPLOAD_DIR, filename)

        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())

        image_data = {"path": filepath}
        updated_image = await cls.update(image_id, **image_data)

        return {"filename": filename, "path": filepath, "image_id": updated_image.id}

    @classmethod
    async def delete_image(cls, image_id: int):
        image = await cls.find_by_id(image_id)

        if not image:
            raise HTTPException(status_code=404, detail="Image not found")

        if os.path.exists(image.path):
            os.remove(image.path)

        await cls.delete(image_id)

        return {"detail": "Image successfully deleted"}
