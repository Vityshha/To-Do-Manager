from fastapi import APIRouter, HTTPException, status
from app.columns.dao import ColumnsDAO
from app.columns.schemas import SColumns, SColumnCreate, SColumnUpdate

router = APIRouter(
    prefix='/columns',
    tags=['Columns'],
)


@router.post('/', response_model=SColumns, status_code=status.HTTP_201_CREATED)
async def create_column(column_data: SColumnCreate):
    column = await ColumnsDAO.add(**column_data.dict())
    return column


@router.get('/', response_model=list[SColumns])
async def get_all_columns():
    columns = await ColumnsDAO.find_all()
    return columns


@router.get('/{column_id}', response_model=SColumns)
async def get_column(column_id: int):
    column = await ColumnsDAO.find_by_id(column_id)
    if not column:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Column not found.")
    return column


@router.put('/{column_id}', response_model=SColumns)
async def update_column(column_id: int, column_data: SColumnUpdate):
    column = await ColumnsDAO.find_by_id(column_id)
    if not column:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Column not found.")
    updated_column = await ColumnsDAO.update(column_id, **column_data.dict(exclude_unset=True))
    return updated_column


@router.delete('/{column_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_column(column_id: int):
    column = await ColumnsDAO.find_by_id(column_id)
    if not column:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Column not found.")
    await ColumnsDAO.delete(column_id)
    return {"detail": "Column successfully deleted."}
