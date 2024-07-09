from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .db import models
from .db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": 'Hello World'}