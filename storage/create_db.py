from sqlmodel import SQLModel
from storage.db import engine

print("CREATING DB.......")

SQLModel.metadata.create_all(engine)
