from fastapi import FastAPI, Depends
from .database import get_db
from sqlalchemy.orm import Session
from .routers import auth

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message" : "Hello world"}



