from fastapi import FastAPI, HTTPException,APIRouter, Depends
from database import Base, engine,get_db
from sqlalchemy.orm import Session


app=FastAPI(title="manager restaurnt")

Base.metadata.create_all(bind=engine)



app.get("/dish")
def get_menu(db:Session=Depends(get_db)):
    return db.all






