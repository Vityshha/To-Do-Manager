from sqlalchemy import Column, Integer, Date, Enum, VARCHAR, TEXT, String
from app.enums import RoleUser
from app.database import Base

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleUser), nullable=False, default=RoleUser.CLIENT)
    date_registration = Column(Date, nullable=True)
    adress = Column(VARCHAR, nullable=True)
    first_name = Column(TEXT, nullable=True)
    last_name = Column(TEXT, nullable=True)
    image_id = Column(Integer, nullable=True)
