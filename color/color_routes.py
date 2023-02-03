from fastapi import APIRouter, status
from sqlmodel import Session
from storage.db import engine

session = Session(bind=engine)

color_router = APIRouter(
    prefix='/color',
    tags=['color']
)


@color_router.get('/', status_code=status.HTTP_200_OK)
async def home():
    return "hello api color!"
