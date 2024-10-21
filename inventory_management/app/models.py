from sqlalchemy import Column, Integer, String
from .database import Base

class Inventory(Base):

    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity = Column(Integer)
