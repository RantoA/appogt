from pyexpat import model
from sqlalchemy.orm import Session
from schemas import schemas
from models import models


async def create_user(db: Session, fonction_id: int, user:schemas.UserCreate):
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


async def get_user(db : Session, user_id : int):
    return db.query(models.Users).filter(models.Users.id==user_id).first()




async def create_fonction(db : Session, fonction : schemas.CreateFonction):
    db_fontion = models.Fonction(nom = fonction.nom)
                                
    db.add(db_fontion)
    await db.commit()
    await db.refresh(db_fontion)
    
    return db_fontion
