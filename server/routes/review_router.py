from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field


class Review(BaseModel):
    id: str
    rating: int
    title: str
    content: str | None = None
    date: str
    reviewer_name: str
    reviewer_location: str | None = None
    verified_purchase: bool
    product_id: str
