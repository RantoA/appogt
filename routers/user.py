from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from base.database import get_db
from . import crud

from schemas import schemas


router = APIRouter(
    prefix="/log_in")

@router.post("/user/{fonction_id}", response_model=schemas.UserCreate, tags=["Inscription"])
def creat_user(fonction_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, fonction_id = fonction_id, user = user)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/user/{user_id}", response_model=schemas.UserCreate, tags=["recuperation"])
def get_user(user_id : int, db : Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
