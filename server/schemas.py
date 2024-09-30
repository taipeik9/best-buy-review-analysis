from datetime import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    title: str
    short_description: str
    avg_rating: float
    rating_count: int
    regular_price: float
    sale_price: float
    category_name: str
    session_id: Union[UUID, None]

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int
    rating: int
    title: str
    content: Union[str, None]
    date: Union[str, datetime]
    reviewer_name: str
    reviewer_location: Union[str, None]
    verified_purchase: bool
    product_id: int
    session_id: Union[UUID, None]

    class Config:
        orm_mode = True


class ScrapingSessionBase(BaseModel):
    id: UUID
    scraping_started: datetime
    scraping_finished: Union[datetime, None]
    done: bool
