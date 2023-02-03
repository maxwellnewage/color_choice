from sqlmodel import SQLModel, Field


class Color(SQLModel, table=True):
    color_id: int = Field(default=None, primary_key=True)
    color: str
