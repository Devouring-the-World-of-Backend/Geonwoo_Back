from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

# Pydantic 모델 정의
class Book(BaseModel):
    id: str #id는 str수도, int일 수도 있으나 장르 구분할수도 있으니 str로 했음!
    title: str
    author: str
    description: Optional[str] = None
    published_year: int

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()