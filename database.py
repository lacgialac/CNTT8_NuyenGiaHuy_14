from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="mysql+pymysql://root:Ghostblade123#@localhost:3306/restaurant_db" 

engine= create_engine(DATABASE_URL)
localhost=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db=localhost
    try:
        yield db
    finally:
        db.close()