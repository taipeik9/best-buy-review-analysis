from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    DateTime,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    short_description = Column(String, nullable=False)
    avg_rating = Column(Float, nullable=False)
    rating_count = Column(Integer, nullable=False)
    regular_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    category_name = Column(String, nullable=False)
    session_id = Column(
        UUID(as_uuid=False), ForeignKey("scraping_sessions.id"), nullable=True
    )

    reviews = relationship("Review", back_populates="product")
    session = relationship("ScrapingSession", back_populates="product")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    reviewer_name = Column(String, nullable=False)
    reviewer_location = Column(String, nullable=True)
    verified_purchase = Column(Boolean, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    session_id = Column(
        UUID(as_uuid=False), ForeignKey("scraping_sessions.id"), nullable=True
    )

    product = relationship("Product", back_populates="reviews")
    session = relationship("ScrapingSession", back_populates="reviews")


class ScrapingSession(Base):
    __tablename__ = "scraping_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    scraping_started = Column(DateTime, server_default=func.now(), nullable=False)
    scraping_finished = Column(DateTime, nullable=True)
    done = Column(Boolean, nullable=False)

    product = relationship("Product", back_populates="session")
    reviews = relationship("Review", back_populates="session")
