from database import Base
from sqlalchemy import Column, String, Integer,Double

class creatTtable(Base):
    __tablename__="menu_items"
    
    id=Column(primary_key=True, autoincrement=True)
    item_name=Column(String(255) ,nullable=False)
    category=Column(String(50),nullable=False)
    price=Column(Double,gt=0, nullable=False)
    status=Column(String(50),nullable=False)
    
    