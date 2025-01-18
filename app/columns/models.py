from sqlalchemy import Column, Integer, TEXT, ForeignKey, Date
from app.database import Base

class Columns(Base):

    __tablename__ = 'columns'

    id = Column(Integer, primary_key=True)
    name = Column(TEXT, nullable=False)
    board_id = Column(ForeignKey('boards.id'), nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=True)
