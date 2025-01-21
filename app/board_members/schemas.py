from pydantic import BaseModel
from app.enums import RoleUser


class SBoardMember(BaseModel):
    id: int
    user_id: int
    board_id: int
    role: RoleUser

    class Config:
        from_attributes = True


class SBoardMemberCreate(BaseModel):
    user_id: int
    board_id: int
    role: RoleUser
