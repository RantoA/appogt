from datetime import date, datetime

from typing import List, Optional

from pydantic import BaseModel, EmailStr

############### Pour l'user #######################
   
class UserCreate(BaseModel):
    im : int
    email : EmailStr
    nom : str
    rubrique : str
    desabled : bool
    description : Optional[str]=None
    
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
    description : Optional[str]=None
    class Config:
        orm_mode=True   

class Foction(CreateFonction):
    id : int

class FonctionOut(CreateFonction):
    pass

############### Pour le saisi #######################

class CreateSaisi(BaseModel):
    montants : float
    description : Optional[str]=None
    intitule : str
    version_id : int
    username : str
    
    class config :
        orm_mode = True

class SaisiBase(CreateSaisi):
    id : int
    datecrea : date
    dateupdate : date

############### Pour la Rubrique #######################

class CreateRubrique(BaseModel):
    intitule : str
    abrev : str
    niveau_ogt : str
    niveau_source : str
    description : Optional[str]=None
    
    class Config:
        orm_mode=True
    
        

class RubriqueBase(CreateRubrique):
    id : int
    datecrea : date
    dateupdate : date
    
    fonction_id : int
    
############### Pour la version #######################

class CreateVersion(BaseModel):
    annee : int
    periode : int
    type_ogt : str
    version : str
    description : Optional[str]=None
    
    class config:
        orm_mode=True

class VersionBase(CreateVersion):
    id : int
