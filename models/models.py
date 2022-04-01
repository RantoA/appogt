from datetime import datetime
from email.policy import default
from http import server
from numbers import Number
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String

from base.database import Base
from routers import fonction


    
class Users(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    nom = Column(String)
    im = Column(Integer)
    email = Column(String)
    rubrique = Column(String)
    description = Column(String)
    desabled = Column(Boolean, nullable=False)
    datecrea = Column(DateTime, default=datetime.utcnow, nullable=False)
    dateupdate = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    fonction_id = Column(Integer, ForeignKey('fonction.id'))



class Fonction(Base):
    __tablename__="fonction"
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    nom = Column(String)
    descriptions = Column(String)


class Saisi(Base):
    __tablename__ = "saisi"
    
    id  = Column(Integer, primary_key=True, autoincrement=True)
    montants = Column(Boolean)
    descriptions = Column(String)
    datecrea = Column(DateTime, default=datetime.utcnow, nullable=False)
    dateupdate = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    intitule = Column(String, ForeignKey('rubrique.intitule'))
    version_id = Column(Integer, ForeignKey('version.id'))
    username = Column(String, ForeignKey('user.nom'))
    
    
    
class Rubrique(Base):
    __tablename__ = "rubrique"
    
    id  = Column(Integer, primary_key=True, autoincrement=True)
    intitule = Column(String)
    abrev = Column(String)
    niveau_source = Column(String)
    niveau_ogt = Column(String)
    description = Column(String)
    datecrea = Column(DateTime, default=datetime.utcnow, nullable=False)
    dateupdate = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    fonction_id = Column(Integer, ForeignKey('fonction.id'))

class Version(Base):
    __tablename__="version"
    
    id  = Column(Integer, primary_key=True, autoincrement=True)
    annee = Column(Integer)
    periode = Column(Integer)
    type_ogt = Column(String)
    Version = Column(String)
    description = Column(String)