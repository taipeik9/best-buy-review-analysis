import scrapy
import json


class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["www.bestbuy.ca"]

    def start_requests(self):
        with open("products.json") as f:
            products = json.load(f)

        for product in products:
            yield scrapy.Request(
                url=f'https://www.bestbuy.ca/api/reviews/v2/products/{product["sku"]}/'
                'reviews?source=all&lang=en-CA&pageSize=100&page=1&sortBy=relevancy',
                callback=self.parse,
            )

    def parse(self, response):
        reviews = json.loads(response.body)["reviews"]

        if reviews:
            for review in reviews:
                yield {
                    "review_id": review["id"],
                    "rating": review["rating"],
                    "title": review["title"],
                    "content": review["comment"],
                    "date": review["submissionTime"],
                    "reviewer_name": review["reviewerName"],
                    "reviewer_location": review["reviewerLocation"],
                    "verified_purchase": review["isVerifiedPurchaser"],
                }
