from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import get_db
from . import crud
from schemas import schemas

router = APIRouter()

@router.post("/fonction", response_model=schemas.FonctionCreate, tags=["Fonction"])
def create_fonction(fonction : schemas.FonctionCreate, db : Session=Depends(get_db)):
    db_fonction = crud.create_fonction(db=db , fonction=fonction)
    return db_fonction