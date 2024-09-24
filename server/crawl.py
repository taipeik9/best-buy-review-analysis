import os
import json

from fastapi import BackgroundTasks

from multiprocessing import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import Spider

from sqlalchemy.orm import Session

from uuid import UUID

from bestbuy.spiders.products import ProductsSpider
from bestbuy.spiders.reviews import ReviewsSpider

from crud import (
    batch_create_product,
    batch_create_reviews,
    create_scraping_session,
    update_scraping_session,
)

import schemas


# This function creates the scraping process (its passed into multiprocess as the target in the function below it)
def scrape(spider: Spider, query: str = None):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(spider, query=query)
    process.start(
        stop_after_crawl=True, install_signal_handlers=False
    )  # the script will block here until all crawling jobs are finished


# This function runs the two scrapers sequentially (from the docs) https://docs.scrapy.org/en/latest/topics/practices.html
def run_scraper(db: Session, query: str, session: UUID):
    for spider in [ProductsSpider, ReviewsSpider]:
        p = Process(target=scrape, args=(spider, query))
        p.start()
        p.join()  # blocks until process is completed

        # opening outputted json files and creating the products then the reviews
    with open("products.json") as f:
        products = json.load(f)
        batch_create_product(db, products=products, session_id=session.id)
    with open("reviews.json") as f:
        reviews = json.load(f)
        batch_create_reviews(db, reviews=reviews, session_id=session.id)

    # Cleanup
    os.remove("products.json")
    os.remove("reviews.json")

    update_scraping_session(db, session.id)


# scrape reviews, this is the controller which is called from the scrape route
def scrape_reviews(
    db: Session, scrape: schemas.Scrape, background_tasks: BackgroundTasks
):
    session = create_scraping_session(db)
    background_tasks.add_task(run_scraper, db=db, query=scrape.query, session=session)

    return {
        "detail": f"Started scraping query {scrape.query}",
        "session_id": session.id,
    }
