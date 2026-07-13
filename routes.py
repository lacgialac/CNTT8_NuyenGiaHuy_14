import services
from sqlalchemy.orm import Session
from schemas import createdish
from database import get_db
from fastapi import APIRouter, Depends

# route=APIRouter(prefix="/dish", tags=["dish"])

# @route.get("/dish")
# def get_dish(db:Depends=Session(get_db)):
#     return db.all


# @route.post("")
# def create_dish(db:Session=Depends(get_db)):
    