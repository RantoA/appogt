from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String

from base.database import Base


    
class Users(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    nom = Column(String)
    im = Column(String)
    email = Column(String)
    rubrique = Column(String)
    description = Column(String)
    datecrea = Column(DateTime, default=datetime.utcnow, nullable=False)
    dateupdate = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    fonction_id = Column(Integer, ForeignKey('fonction.id'))



class Fonction(Base):
    __tablename__="fonction"
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    nom = Column(String)


