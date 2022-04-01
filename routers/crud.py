from pyexpat import model
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from routers import user
from schemas import schemas
from models import models

################################ USERS ####################################

async def create_user(db, fonction_id: int, user:schemas.UserCreate):
    db_user= models.Users(im = user.im, 
                          email = user.email, 
                          nom = user.nom, 
                          rubrique = user.rubrique,
                          description = user.description,
                          fonction_id=fonction_id)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db , user_id : int):
    rep = await db.execute(select(models.Users).where(models.Users.id==user_id))
    return rep.scalars().all()


################################ FONCTIONS ####################################


async def create_fonction(db , fonction : schemas.CreateFonction):
    db_fontion = models.Fonction(nom = fonction.nom,
                                 description = fonction.description)
                                
    db.add(db_fontion)
    await db.commit()
    await db.refresh(db_fontion)
    
    return db_fontion


################################ RUBRIQUES ####################################


async def CreateRubrique(db, fonction_id: int, rubrique: schemas.CreateRubrique):
    db_rubrique = models.Rubrique(intitule = rubrique.intitule,
                                  abrev = rubrique.abrev,
                                  niveau_ogt = rubrique.niveau_ogt,
                                  niveau_source = rubrique.niveau_source,
                                  description = rubrique.description,
                                  fonction_id = fonction_id)
    db.add(db_rubrique)
    await db.commit()
    await db.refresh(db_rubrique)
    

async def get_rubrique(db , rubrique_id : int):
    rep = await db.execute(select(models.Rubrique).where(models.Rubrique.id==rubrique_id))
    return rep.scalars().all()