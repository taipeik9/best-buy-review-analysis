from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Request,
    BackgroundTasks,
)
from sqlalchemy.orm import Session

from typing import List

import crud
import models
import schemas
from database import SessionLocal, engine
from services.crawl import run_scraper

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=List[schemas.ProductBase])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{product_id}", response_model=List[schemas.ProductBase])
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


@app.post("/reviews/", response_model=dict[str:str])
async def scrape(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    if "query" not in body:
        raise HTTPException(status_code=400, detail="Query parameter is missing")

    background_tasks.add_task(run_scraper, query=body["query"])

    return {"detail": f"Started scraping products with search query: {body['query']}"}
