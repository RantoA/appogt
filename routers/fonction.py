from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from base.database import get_db
from . import crud
from schemas import schemas

router = APIRouter()

@router.post("/fonction", tags=["Fonction"], response_model=schemas.FonctionOut)
async def create_fonction(fonction : schemas.CreateFonction, db : AsyncSession=Depends(get_db)):
    db_fonction = await crud.create_fonction(db=db , fonction=fonction)
    return db_fonction