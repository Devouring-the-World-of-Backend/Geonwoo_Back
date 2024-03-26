from typing import Dict, Optional
from fastapi import FastAPI, HTTPException

# Pydantic 모델 정의
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    published_year: int

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# Fake DB를 모의로 구현
fake_db: Dict[str, Book] = {}

@app.post("/books/")
async def create_book(book: Book):
    if book.id in fake_db:
        raise HTTPException(status_code=400, detail="Book already exists")
    fake_db[book.id] = book
    return book

@app.get("/books/")
async def read_books():
    return list(fake_db.values())

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    if book_id not in fake_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return fake_db[book_id]

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    if book_id not in fake_db:
        raise HTTPException(status_code=404, detail="Book not found")
    fake_db[book_id] = book
    return book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id not in fake_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del fake_db[book_id]
    return {"message": "Book deleted"}