from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    title: str
    short_description: str
    avg_rating: float
    rating_count: int
    reg_price: float
    sale_price: float
    category_name: str

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int
    rating: int
    title: str
    content: str
    date: str
    reviewer_name: str
    reviewer_location: str
    verified_purchase: bool
    product_id: int

    class Config:
        orm_mode = True
