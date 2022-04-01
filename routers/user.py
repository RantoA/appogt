from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from base.database import get_db
from . import crud

from schemas.schemas import UserCreate, UserOut


router = APIRouter()

@router.post("/log_in/user/fonction_id={fonction_id}", tags=["Inscription"], response_model=UserOut)
async def creat_user(fonction_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.create_user(db=db, fonction_id = fonction_id, user = user)

    return db_user

@router.get("/user/user_id={user_id}", tags=["recuperation"], response_model=List[UserOut])
async def get_user(user_id : int, db : AsyncSession = Depends(get_db)):
     #db_user = await crud.get_user(db, user_id=user_id)
    try:
        return await crud.get_user(db, user_id=user_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
