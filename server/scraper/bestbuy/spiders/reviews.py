import scrapy
import json


# Spider that crawls through Best Buy Reviews
class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["www.bestbuy.ca"]

    def start_requests(self):
        # Opening the products json to find reviews for them
        with open("products.json") as f:
            products = json.load(f)

        for product in products:
            yield scrapy.Request(
                url=f'https://www.bestbuy.ca/api/reviews/v2/products/{product["sku"]}/'
                'reviews?source=all&lang=en-CA&pageSize=100&page=1&sortBy=relevancy',
                callback=self.parse,
                meta={"sku": product["sku"]},
            )

    # Parsing the review pages
    def parse(self, response):
        # Trying to find page number in meta data, if it isn't there, then this is the start page
        try:
            page = response.meta["page_number"]
        except KeyError:
            page = 1

        reviews = json.loads(response.body)["reviews"]

        # Check, if reviews is empty then we are at the end and there is nothing else to yield
        if reviews:
            for review in reviews:
                yield {
                    "review_id": review["id"],
                    "rating": review["rating"],
                    "title": review["title"],
                    "content": review["comment"],
                    "date": review["submissionTime"],
                    "reviewer_name": review["reviewerName"],
                    "reviewer_location": review.get("reviewerLocation", ""),
                    "verified_purchase": review["isVerifiedPurchaser"],
                }

            yield response.follow(
                url=f'https://www.bestbuy.ca/api/reviews/v2/products/{response.request.meta["sku"]}/'
                f'reviews?source=all&lang=en-CA&pageSize=100&page={page}&sortBy=relevancy'
            )
