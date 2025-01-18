from sqlalchemy import Column, Integer, Date, String
from app.database import Base

class Boards(Base):

    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)