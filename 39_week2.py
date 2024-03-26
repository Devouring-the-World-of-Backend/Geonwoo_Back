from typing import Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

# Pydantic 모델 정의
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    published_year: int

    # Custom validator for the 'published_year'
    @validator('published_year')
    def validate_published_year(cls, value):
        if not (1900 <= value <= 2024):
            raise ValueError('The published year must be between 1900 and 2100.')
        return value

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()