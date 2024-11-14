from sqlalchemy import Column, Integer, Date

from app.database import Base

class Deadlines(Base):

    __tablename__ = 'deadlines'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)