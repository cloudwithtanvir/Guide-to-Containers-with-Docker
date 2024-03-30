from fastapi import FastAPI, Depends
from typing import List  # Import List from typing
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/books/", response_model=models.Book)
def create_new_book(book: models.Book, db: Session = Depends(SessionLocal)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[models.Book])
def read_all_books(db: Session = Depends(SessionLocal)):
    return crud.get_books(db=db)
