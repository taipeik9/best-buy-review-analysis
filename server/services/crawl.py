import os

from twisted.internet import reactor, defer

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from bestbuy.spiders.products import ProductsSpider
from bestbuy.spiders.reviews import ReviewsSpider

from .upload_scraped_items import upload_products_and_reviews


# This function runs the two scrapers sequentially (from the docs) https://docs.scrapy.org/en/latest/topics/practices.html
def run_scraper(query):
    # Getting project settings and configuring logger
    settings = get_project_settings()
    configure_logging(settings)
    runner = CrawlerRunner(settings)

    # Function to run crawlers sequentially
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ProductsSpider, query)
        yield runner.crawl(ReviewsSpider)
        reactor.stop()

    crawl()
    reactor.run()  # script blocks here until the last crawl call is finished

    upload_products_and_reviews("products.json", "reviews.json")

    # Cleanup
    os.remove("products.json")
    os.remove("reviews.json")
