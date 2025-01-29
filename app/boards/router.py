from fastapi import APIRouter, HTTPException, status
from app.boards.dao import BoardsDAO
from app.boards.schemas import SBoards, SBoardCreate, SBoardUpdate
from datetime import datetime

router = APIRouter(
    prefix='/boards',
    tags=['Boards'],
)


@router.post('/', response_model=SBoards, status_code=status.HTTP_201_CREATED)
async def create_board(board_data: SBoardCreate):
    existing_board = await BoardsDAO.find_by_name(board_data.name)
    if existing_board:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Board with this name already exists.")
    board = await BoardsDAO.add(name=board_data.name, created_at=datetime.utcnow())
    return board


@router.get('/', response_model=list[SBoards])
async def get_all_boards():
    boards = await BoardsDAO.find_all()
    return boards


@router.get('/{board_id}', response_model=SBoards)
async def get_board(board_id: int):
    board = await BoardsDAO.find_by_id(board_id)
    if not board:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Board not found.")
    return board


@router.put('/{board_id}', response_model=SBoards)
async def update_board(board_id: int, board_data: SBoardUpdate):
    board = await BoardsDAO.find_by_id(board_id)
    if not board:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Board not found.")
    updated_board = await BoardsDAO.update(board_id, **board_data.dict(exclude_unset=True))
    return updated_board


@router.delete('/{board_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_board(board_id: int):
    board = await BoardsDAO.find_by_id(board_id)
    if not board:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Board not found.")
    await BoardsDAO.delete(board_id)
    return {"detail": "Board successfully deleted."}
