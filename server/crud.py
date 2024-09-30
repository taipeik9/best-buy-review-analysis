from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from dateutil import parser
from uuid import UUID


import models
import schemas


# get product by id
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


# get all products
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


# get products by session id
def get_products_by_session_id(db: Session, session_id: str):
    return (
        db.query(models.Product)
        .filter(models.Product.session_id == UUID(session_id))
        .all()
    )


# create product
def create_product(
    db: Session,
    product: schemas.ProductBase,
    on_exist_skip: bool = False,
    session_id: UUID = None,
):
    if get_product(db, product_id=product.id) is not None:
        if not on_exist_skip:
            raise HTTPException(status_code=409, detail="Product ID already exists")
        else:
            return False

    db_product = models.Product(
        id=product.id,
        title=product.title,
        short_description=product.short_description,
        avg_rating=product.avg_rating,
        rating_count=product.rating_count,
        regular_price=product.regular_price,
        sale_price=product.sale_price,
        category_name=product.category_name,
        session_id=session_id,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# create products
def batch_create_product(
    db: Session, products: list[schemas.ProductBase], session_id: UUID = None
):
    db_products = []

    for product in products:
        product["session_id"] = session_id

        product_schema = (
            schemas.ProductBase.model_validate(product)
            if type(product) is dict
            else product
        )
        temp_db_product = create_product(
            db, product=product_schema, on_exist_skip=True, session_id=session_id
        )
        if temp_db_product:
            db_products.append(temp_db_product)

    return db_products


# get review by id
def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()


# get all reviews
def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Review)
        .order_by(models.Review.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# get reviews by session id
def get_reviews_by_session_id(
    db: Session, session_id: str, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.Review)
        .filter(models.Review.session_id == UUID(session_id))
        .order_by(models.Review.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# get reviews by product id
def get_reviews_by_product_id(
    db: Session, product_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.Review)
        .filter(models.Review.product_id == product_id)
        .order_by(models.Review.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# create review
def create_review(
    db: Session,
    review: schemas.ReviewBase,
    on_exist_skip: bool = False,
    session_id: UUID = None,
):
    if get_review(db, review_id=review.id) is not None:
        if not on_exist_skip:
            raise HTTPException(status_code=409, detail="Review ID already exists")
        else:
            return False

    db_review = models.Review(
        id=review.id,
        rating=review.rating,
        title=review.title,
        content=review.content,
        date=parser.parse(review.date),
        reviewer_name=review.reviewer_name,
        reviewer_location=review.reviewer_location,
        verified_purchase=review.verified_purchase,
        product_id=review.product_id,
        session_id=session_id,
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


# create reviews
def batch_create_reviews(
    db: Session, reviews: list[schemas.ReviewBase], session_id: UUID = None
):
    db_reviews = []
    for review in reviews:
        review["session_id"] = session_id

        review_schema = (
            schemas.ReviewBase.model_validate(review)
            if type(review) is dict
            else review
        )
        temp_db_review = create_review(
            db, review=review_schema, on_exist_skip=True, session_id=session_id
        )
        if temp_db_review:
            db_reviews.append(temp_db_review)

    return db_reviews


# get scraping session by id
def get_scraping_session(db: Session, session_id: UUID):
    return (
        db.query(models.ScrapingSession)
        .filter(models.ScrapingSession.id == session_id)
        .first()
    )


# get all scraping sessions
def get_scraping_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ScrapingSession).offset(skip).limit(limit).all()


# create scraping session
def create_scraping_session(db: Session):
    db_scraping_session = models.ScrapingSession(scraping_finished=None, done=False)

    db.add(db_scraping_session)
    db.commit()
    db.refresh(db_scraping_session)

    return db_scraping_session


# update scraping session
def update_scraping_session(db: Session, session_id: UUID):
    scraping_session = get_scraping_session(db, session_id=session_id)

    if not scraping_session:
        raise HTTPException(status_code=404, detail="Session ID not found")

    scraping_session.done = True
    scraping_session.scraping_finished = datetime.now()

    db.commit()
    db.refresh(scraping_session)

    return scraping_session
