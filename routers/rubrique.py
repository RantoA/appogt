from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from base.database import get_db
from . import crud
from schemas.schemas import CreateRubrique

router = APIRouter(
    tags=["Rubrique"]
    )

@router.post("/rubrique/{fonction_id}", response_model=CreateRubrique)
async def  Create_rubrique(fonction_id : int, rubrique : CreateRubrique, db : AsyncSession=Depends(get_db)):
    db_rubrique = await crud.CreateRubrique(db=db, fonction_id=fonction_id, rubrique=rubrique)
    return db_rubrique

@router.get("/Rubrique/id={rubrique_id}", response_model= List[CreateRubrique])
async def get_rubrique(rubrique_id : int, db : AsyncSession=Depends(get_db)):
    try:
        return await crud.get_rubrique(db, rubrique_id=rubrique_id)
    except Exception as error :
        raise HTTPException(400, detail =str(error))
    
    


