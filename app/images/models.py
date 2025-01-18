from sqlalchemy import Column, Integer
from app.database import Base

class Images(Base):

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
