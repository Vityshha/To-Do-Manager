from sqlalchemy import Column, Integer, Enum, TEXT, BOOLEAN
from app.enums import DoorsLoops
from app.database import Base

class Descriptions(Base):

    __tablename__ = 'descriptions'

    id = Column(Integer, primary_key=True)
    doors = Column(Integer, nullable=False)
    loops = Column(Enum(DoorsLoops), nullable=True)
    platbands = Column(BOOLEAN, nullable=True)
    description = Column(TEXT, nullable=True)
