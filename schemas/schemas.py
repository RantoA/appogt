from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr

############### Pour l'user #######################
   
class UserCreate(BaseModel):
    im : int
    email : EmailStr
    nom : str
    rubrique : str
    description : str
    
    class Config:
        orm_mode=True

class UserBase(UserCreate):
    id : int
    datecrea : date
    dateupdate : date
    
    fonction_id : int
    
class UserOut(UserCreate):
    pass


############### Pour la fonction #######################

class CreateFonction(BaseModel):
    nom : str

    class Config:
        orm_mode=True   

class Foction(CreateFonction):
    id : int

class FonctionOut(CreateFonction):
    pass

############### Pour le saisi #######################