from sqlmodel import SQLModel
from storage.db import engine
import models

print("CREATING DB.......")

SQLModel.metadata.create_all(engine)
