import scrapy
import json


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.bestbuy.ca"]
    query = "computers"
    start_page = 1
    max_pages = 10
    start_urls = [
        f"https://www.bestbuy.ca/api/v2/json/search?lang=en-CA&page={start_page}&pageSize=100&query={query}"
    ]

    def parse(self, response):
        try:
            page = response.meta["page_number"]
        except KeyError:
            page = 1

        products = json.loads(response.body)["products"]

        if products and page <= self.max_pages:
            for product in products:
                if product["customerRatingCount"] > 0:
                    yield {
                        "sku": product["sku"],
                        "title": product["name"],
                        "short_description": product["shortDescription"],
                        "avg_rating": product["customerRating"],
                        "rating_count": product["customerRatingCount"],
                        "regular_price": product["regularPrice"],
                        "sale_price": product["salePrice"],
                        "category_name": product["categoryName"],
                    }

            yield response.follow(
                url=f"https://www.bestbuy.ca/api/v2/json/search?lang=en-CA&page={page}&pageSize=100&query={self.query}",
                meta={"page_number": page + 1},
                callback=self.parse,
            )
