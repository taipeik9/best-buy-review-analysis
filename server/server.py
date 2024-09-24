from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    BackgroundTasks,
)
from sqlalchemy.orm import Session

from uuid import UUID

import crud
import crawl
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=list[schemas.ProductBase])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{product_id}", response_model=list[schemas.ProductBase])
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} was not found"
        )
    return product


@app.post("/product/", response_model=schemas.ProductBase)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    return crud.create_product(db, product=product)


@app.post("/products/", response_model=list[schemas.ProductBase])
def batch_create_products(
    products: list[schemas.ProductBase], db: Session = Depends(get_db)
):
    return crud.batch_create_product(db, products=products)


@app.post("/review/")
def create_review(review: schemas.ReviewBase, db: Session = Depends(get_db)):
    return crud.create_review(db, review=review)


@app.post("/reviews/")
def create_reviews(reviews: list[schemas.ReviewBase], db: Session = Depends(get_db)):
    return crud.batch_create_reviews(db, reviews=reviews)


@app.post("/scrape/", response_model=dict)
async def scrape_reviews(
    scrape: schemas.Scrape,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    return crawl.scrape_reviews(db, scrape=scrape, background_tasks=background_tasks)


@app.post("/session/", response_model=schemas.ScrapingSessionBase)
def create_session(db: Session = Depends(get_db)):
    return crud.create_scraping_session(db)


@app.put("/session/{session_id}")
def update_session(session_id: UUID, db: Session = Depends(get_db)):
    return crud.update_scraping_session(db, session_id=session_id)
