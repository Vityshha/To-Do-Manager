from sqlalchemy import Column, Integer, Enum, FLOAT, ForeignKey
from app.enums import LevelWorker
from app.database import Base

class Workers(Base):

    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True)
    worker_id = Column(ForeignKey('users.id'), nullable=False)
    level_worker = Column(Enum(LevelWorker), nullable=False, default=LevelWorker.JUNIOR)
    rating = Column(FLOAT, nullable=True)
    reviews = Column(Integer, nullable=True)
