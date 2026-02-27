from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from fastapi.staticfiles import StaticFiles

DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class LibraryDB(Base):
    __tablename__ = "libraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    books = relationship("BookDB", back_populates="library")

class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    isbn_code = Column(String, unique=True)
    library_id = Column(Integer, ForeignKey("libraries.id"))

    library = relationship("LibraryDB", back_populates="books")


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)  


Base.metadata.create_all(bind=engine)



class User(BaseModel):
    username: str
    password: str


class Book(BaseModel):
    title: str
    isbn_code: str

app = FastAPI()



@app.post("/api/register")
def register(user: User):
    db = SessionLocal()

    existing_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserDB(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()

    return {"message": "User registered successfully"}


@app.get("/api/login")
def login(username: str, password: str):
    db = SessionLocal()

    user = db.query(UserDB).filter(UserDB.username == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}


@app.post("/api/books")
def add_book(book: Book):
    db = SessionLocal()

    library = db.query(LibraryDB).first()
    if not library:
        library = LibraryDB(name="Central Library")
        db.add(library)
        db.commit()
        db.refresh(library)

    new_book = BookDB(
        title=book.title,
        isbn_code=book.isbn_code,
        library_id=library.id
    )

    db.add(new_book)
    db.commit()

    return {"message": "Book added successfully"}


@app.get("/api/books")
def get_books():
    db = SessionLocal()
    books = db.query(BookDB).all()

    return books

app.mount("/", StaticFiles(directory="frontend/static", html=True), name="static")