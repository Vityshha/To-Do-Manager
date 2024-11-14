from sqlalchemy import Column, Integer, Date, Enum, JSON, FLOAT, ForeignKey
from app.enums import OrderStatus, OrderComplexity
from app.database import Base

class Orders(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    date_creation = Column(Date, nullable=False)
    order_status = Column(Enum(OrderStatus), nullable=False)
    description_id = Column(ForeignKey('descriptions.id'), nullable=False)
    reviews_id = Column(ForeignKey('reviews.id'), nullable=True)
    deadlines_id = Column(ForeignKey('deadlines.id'), nullable=False)
    complexity = Column(Enum(OrderComplexity), nullable=True)
    workers = Column(JSON, nullable=False)
    price = Column(FLOAT, nullable=False)
