from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    short_description = Column(String, nullable=False)
    avg_rating = Column(Float, nullable=False)
    rating_count = Column(Integer, nullable=False)
    reg_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    category_name = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="product")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    reviewer_name = Column(String, nullable=False)
    reviewer_location = Column(String, nullable=True)
    verified_purchase = Column(Boolean, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    product = relationship("Product", back_populates="reviews")


# class ScrapingSession(Base):
#     __tablename__ = "scraping_sessions"
