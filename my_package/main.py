from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud,model
from .database import SessionLocal,engine 

models.Base.metadata.create_all(engine)


def get_db():
	db=SessionLocal()
	try:
		yield db 
    finally :
    	db.close()