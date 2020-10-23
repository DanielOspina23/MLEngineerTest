from sqlalchemy import Column, Integer, BigInteger, Float, DateTime
import datetime as dt
from database.db import Base


class PredModel(Base):
    __tablename__ = 'taken_order'

    id = Column(BigInteger, primary_key=True, unique=True, index=True)
    order_id = Column(BigInteger, nullable=False)
    store_id = Column(BigInteger, nullable=False)
    to_user_distance = Column(Float, nullable=False)
    to_user_elevation = Column(Float, nullable=False)
    total_earning = Column(Integer, nullable=False)
    order_date = Column(DateTime, nullable=False)
    taken_probability = Column(Float, nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    def __init__(self, order_id, store_id, to_user_distance, to_user_elevation, total_earning, order_date, taken_probability):
        self.order_id = order_id
        self.store_id = store_id
        self.to_user_distance = to_user_distance
        self.to_user_elevation = to_user_elevation
        self.total_earning = total_earning
        self.order_date = order_date
        self.taken_probability = taken_probability
