import scrapy
import json

from ..items import Product


# Spider that crawls through Best Buy Products
class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.bestbuy.ca"]
    query = "computers"

    # Initializing with custom args
    def __init__(self, query=None, start_page=1, max_pages=10, **kwargs):
        if query:
            self.start_urls = [
                f"https://www.bestbuy.ca/api/v2/json/search?lang=en-CA&page={start_page}&pageSize=100&query={query}"
            ]
            self.start_page = start_page
            self.max_pages = max_pages
        else:
            raise Exception("Query must be provided")

    # Parse through product pages
    def parse(self, response):
        # Trying to find page number in meta data, if it isn't there, then this is the start page
        try:
            page = response.meta["page_number"]
        except KeyError:
            page = self.start_page

        products = json.loads(response.body)["products"]

        # Yielding products until page limit reached or there are no more
        if products and page <= self.max_pages:
            for product in products:
                # Ignoring all products which don't have reviews
                if product["customerRatingCount"] > 0:
                    productItem = Product()

                    productItem["id"] = product["sku"]
                    productItem["title"] = product["name"]
                    productItem["short_description"] = product["shortDescription"]
                    productItem["avg_rating"] = product["customerRating"]
                    productItem["rating_count"] = product["customerRatingCount"]
                    productItem["regular_price"] = product["regularPrice"]
                    productItem["sale_price"] = product["salePrice"]
                    productItem["category_name"] = product["categoryName"]

                    yield productItem

            yield response.follow(
                url=f"https://www.bestbuy.ca/api/v2/json/search?lang=en-CA&page={page + 1}&pageSize=100&query={self.query}",
                meta={"page_number": page + 1},
                callback=self.parse,
            )
