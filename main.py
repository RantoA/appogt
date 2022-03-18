from fastapi import FastAPI
from routers import fonction, user
from models import models
from base.config import settings
from base.database import init_db, get_db
from models.models import Users
from sqlalchemy.orm import Session

app = FastAPI(title="appOGT")

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(user.router)
app.include_router(fonction.router)

@app.get("/", tags=["Accueil"])
async def appOgt():
    return{"msg": "WELCOM TO APPOGT"}
