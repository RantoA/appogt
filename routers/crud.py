from pyexpat import model
from sqlalchemy.orm import Session
from schemas import schemas
from models import models


def create_user(db: Session, fonction_id: int, user:schemas.UserCreate):
    db_user= models.Users(im = user.im, 
                          email = user.email, 
                          nom = user.nom, 
                          rubrique = user.rubrique,
                          description = user.description,
                          fonction_id=fonction_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db : Session, user_id : int):
    return db.query(models.Users).filter(models.Users.id==user_id).first()




def create_fonction(db : Session, fonction : schemas.FonctionCreate):
    db_fontion = models.Fonction(nom = fonction.nom)
                                
    db.add(db_fontion)
    db.commit()
    db.refresh(db_fontion)
