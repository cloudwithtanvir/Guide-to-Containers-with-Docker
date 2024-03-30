from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    pages: int

    class Config:
        orm_mode = True
