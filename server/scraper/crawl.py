from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import multiprocessing

from bestbuy.spiders.products import ProductsSpider
from bestbuy.spiders.reviews import ReviewsSpider


def run_crawler(settings, spider):
    process = CrawlerProcess(settings)
    process.crawl(spider)
    process.start()


if __name__ == "__main__":
    settings = get_project_settings()
    settings["FEED_FORMAT"] = "json"
    settings["FEED_EXPORT_ENCODING"] = "utf-8"

    spiders = [ProductsSpider, ReviewsSpider]

    for i, spider in enumerate(spiders):
        settings["FEED_URI"] = "products.json" if i == 0 else "reviews.json"

        p = multiprocessing.Process(target=run_crawler, args=(settings, spider))
        p.start()
        p.join()
