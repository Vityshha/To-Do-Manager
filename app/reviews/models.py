from sqlalchemy import Column, Integer, Enum, TEXT
from app.enums import RatingOrder
from app.database import Base

class Reviews(Base):

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    reviews = Column(TEXT, nullable=False)
    rating = Column(Enum(RatingOrder), nullable=False)
