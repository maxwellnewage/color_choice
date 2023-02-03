from sqlmodel import SQLModel
from storage.db import engine
import color
import vote

print("CREATING DB.......")

SQLModel.metadata.create_all(engine)
