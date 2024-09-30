from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    BackgroundTasks,
)
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from uuid import UUID

import crud
import crawl
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get all products
@app.get("/products/", response_model=list[schemas.ProductBase])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


# get product by id
@app.get("/products/{product_id}/", response_model=schemas.ProductBase)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} was not found"
        )
    return product


# get products by session id
@app.get("/sessions/{session_id}/products/", response_model=list[schemas.ProductBase])
def read_products_by_session_id(session_id: str, db: Session = Depends(get_db)):
    return crud.get_products_by_session_id(db, session_id=session_id)


# create product
@app.post("/product/", response_model=schemas.ProductBase)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    return crud.create_product(db, product=product)


# batch create products
@app.post("/products/", response_model=list[schemas.ProductBase])
def batch_create_products(
    products: list[schemas.ProductBase], db: Session = Depends(get_db)
):
    return crud.batch_create_product(db, products=products)


# get review by id
@app.get("/reviews/{review_id}/", response_model=schemas.ReviewBase)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = crud.get_review(db, review_id=review_id)
    if review is None:
        raise HTTPException(
            status_code=404, detail=f"Review with review id {review_id} was not found"
        )
    return review


# get reviews by session id
@app.get("/sessions/{session_id}/reviews/", response_model=list[schemas.ReviewBase])
def read_reviews_by_session_id(
    session_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_reviews_by_session_id(
        db, session_id=session_id, skip=skip, limit=limit
    )


# get reviews by product id
@app.get("/products/{product_id}/reviews/", response_model=list[schemas.ReviewBase])
def read_reviews_by_product_id(
    product_id, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_reviews_by_product_id(
        db, product_id=product_id, skip=skip, limit=limit
    )


# get all reviews
@app.get("/reviews/", response_model=list[schemas.ReviewBase])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reviews(db, skip=skip, limit=limit)


# create review
@app.post("/review/", response_model=schemas.ReviewBase)
def create_review(review: schemas.ReviewBase, db: Session = Depends(get_db)):
    return crud.create_review(db, review=review)


# batch create reviews
@app.post("/reviews/", response_model=list[schemas.ReviewBase])
def create_reviews(reviews: list[schemas.ReviewBase], db: Session = Depends(get_db)):
    return crud.batch_create_reviews(db, reviews=reviews)


# scrape reviews by query
@app.post("/scrape/{query}/", response_model=dict)
async def scrape_reviews(
    query: str,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    return crawl.scrape_reviews(db, query=query, background_tasks=background_tasks)


# get sesssion by id
@app.get("/sessions/{session_id}/", response_model=schemas.ScrapingSessionBase)
def read_session(session_id: UUID, db: Session = Depends(get_db)):
    return crud.get_scraping_session(db, session_id=session_id)


# get all sesssions
@app.get("/sessions/", response_model=list[schemas.ScrapingSessionBase])
def read_sessions(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_scraping_sessions(db, skip=skip, limit=limit)


# create session
@app.post("/session/", response_model=schemas.ScrapingSessionBase)
def create_session(db: Session = Depends(get_db)):
    return crud.create_scraping_session(db)


# get session by id
@app.put("/sessions/{session_id}/")
def update_session(session_id: UUID, db: Session = Depends(get_db)):
    return crud.update_scraping_session(db, session_id=session_id)
