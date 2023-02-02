from typing import List
from fastapi import FastAPI, status
from sqlmodel import Session, select
from storage.db import engine
from storage.models import Vote

app = FastAPI()

session = Session(bind=engine)


@app.get('/', status_code=status.HTTP_200_OK)
async def home():
    return "hello api!"


@app.get('/votes', response_model=List[Vote], status_code=status.HTTP_200_OK)
async def get_all_votes():
    return session.exec(select(Vote)).all()
