from sqlalchemy import Column, Integer, Date, TEXT, String, ForeignKey
from app.database import Base
from datetime import date

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(Date, nullable=False, default=date.today())
    first_name = Column(TEXT, nullable=True)
    last_name = Column(TEXT, nullable=True)
    image_id = Column(Integer, nullable=True)
