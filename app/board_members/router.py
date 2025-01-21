from fastapi import APIRouter, HTTPException, status
from app.board_members.dao import BoardMembersDAO
from app.board_members.schemas import SBoardMember, SBoardMemberCreate

router = APIRouter(
    prefix='/board_members',
    tags=['Board members'],
)


@router.post('/', response_model=SBoardMember, status_code=status.HTTP_201_CREATED)
async def add_board_member(member_data: SBoardMemberCreate):
    existing_member = await BoardMembersDAO.find_by_user_and_board(member_data.user_id, member_data.board_id)
    if existing_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already a member of the board.")
    member = await BoardMembersDAO.add(**member_data.dict())
    return member


@router.get('/{board_id}', response_model=list[SBoardMember])
async def get_board_members(board_id: int):
    members = await BoardMembersDAO.find_all_by_board(board_id)
    if not members:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No members found for this board.")
    return members


@router.delete('/{member_id}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_board_member(member_id: int):
    member = await BoardMembersDAO.find_by_id(member_id)
    if not member:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Board member not found.")
    await BoardMembersDAO.delete(member_id)
    return {"detail": "Board member successfully removed."}
