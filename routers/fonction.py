from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from base.database import get_db
from . import crud
from schemas import schemas

router = APIRouter()

@router.post("/fonction", tags=["Fonction"])
async def create_fonction(fonction : schemas.CreateFonction, db : Session=Depends(get_db)):
    db_fonction = await crud.create_fonction(db=db , fonction=fonction)
    return db_fonction