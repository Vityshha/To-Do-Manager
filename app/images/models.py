from sqlalchemy import Column, Integer, String
from app.database import Base

class Images(Base):

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    path = Column(String(255), nullable=True)
