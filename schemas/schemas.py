from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr

############### Pour l'user #######################
   
class UserCreate(BaseModel):
    im : str
    email : EmailStr
    nom : str
    rubrique : str
    description : str

class UserBase(UserCreate):
    id : int
    datecrea : date
    dateupdate : date
    
    fonction_id : int
    
    class Config:
        orm_mode=True


############### Pour la fonction #######################

class FonctionCreate(BaseModel):
    nom : str
   

class FonctionBase(FonctionCreate):
    id : int

    class Config:
        orm_mode=True