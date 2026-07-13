from fastapi import FastAPI, HTTPException,APIRouter, Depends
from database import Base, engine,get_db


app=FastAPI(title="manager restaurnt")

Base.metadata.create_all(bind=engine)










