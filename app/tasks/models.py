from sqlalchemy import Column, Integer, Enum, TEXT, BOOLEAN, Date, ForeignKey
from app.enums import TasksStatus
from app.database import Base

class Tasks(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=True)
    status = Column(Enum(TasksStatus), nullable=False)
    deadline = Column(Date, nullable=True)
    created_at = Column(Date, nullable=True)
    column_id = Column(ForeignKey('columns.id'), nullable=False)
    position = Column(Integer, nullable=False)
