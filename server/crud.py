from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List


import models
import schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductBase):
    if get_product(db, product_id=product.id) is not None:
        raise HTTPException(status_code=409, detail="Product ID already exists")

    db_product = models.Product(
        id=product.id,
        title=product.title,
        short_description=product.short_description,
        avg_rating=product.avg_rating,
        rating_count=product.rating_count,
        reg_price=product.reg_price,
        sale_price=product.sale_price,
        category_name=product.category_name,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def batch_create_product(db: Session, product: List[schemas.ProductBase]):
    pass
