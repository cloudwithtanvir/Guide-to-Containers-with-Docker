from sqlalchemy.orm import Session
from . import models
from .models import Book

def create_book(db: Session, book: models.BookCreate):
    db_book = Book(title=book.title, author=book.author, pages=book.pages)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()
