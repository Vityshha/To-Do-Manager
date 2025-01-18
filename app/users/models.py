from sqlalchemy import Column, Integer, Date, TEXT, String
from app.database import Base

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(Date, nullable=True)
    first_name = Column(TEXT, nullable=True)
    last_name = Column(TEXT, nullable=True)
    image_id = Column(Integer, nullable=True)
