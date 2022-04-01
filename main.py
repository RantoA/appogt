from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers import fonction, rubrique, user
from models import models
from base.config import settings
from base.database import init_db, get_db
from models.models import Users
from sqlalchemy.orm import Session

app = FastAPI(title="appOGT")

@app.on_event("startup")
async def on_startup():
    await init_db()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/", tags=["Accueil"])
async def appOgt():
    return{"msg": "WELCOM TO APPOGT"}

app.include_router(user.router)
app.include_router(fonction.router)
app.include_router(rubrique.router)
