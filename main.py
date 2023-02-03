from typing import List
from fastapi import FastAPI, status
from color.color_routes import color_router
from vote.vote_routes import vote_router

app = FastAPI()

app.include_router(color_router)
app.include_router(vote_router)


@app.get('/', status_code=status.HTTP_200_OK)
async def home():
    return "hello api!"

# session = Session(bind=engine)

# @app.get('/votes', response_model=List[Vote], status_code=status.HTTP_200_OK)
# async def get_all_votes():
#     return session.exec(select(Vote)).all()
