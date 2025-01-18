from sqlalchemy import Column, Integer, Enum, ForeignKey
from app.enums import RoleUser
from app.database import Base

class BoardMembers(Base):

    __tablename__ = 'board_members'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    board_id = Column(ForeignKey('boards.id'), nullable=False)
    role = Column(Enum(RoleUser), nullable=False)
