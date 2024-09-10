import scrapy
import json

from ..items import Review


# Spider that crawls through Best Buy Reviews
class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["www.bestbuy.ca"]
    count = 0
    total_products = 0

    def start_requests(self):
        # Opening the products json to find reviews for them
        with open("products.json") as f:
            products = json.load(f)
        self.total_products = len(products)

        for product in products:
            yield scrapy.Request(
                url=f'https://www.bestbuy.ca/api/reviews/v2/products/{product["id"]}/'
                'reviews?source=all&lang=en-CA&pageSize=100&page=1&sortBy=relevancy',
                callback=self.parse,
                meta={"id": product["id"]},
            )

    # Parsing the review pages
    def parse(self, response):
        # Trying to find page number in meta data, if it isn't there, then this is the start page
        try:
            page = response.meta["page"]
        except KeyError:
            page = 1

        reviews = json.loads(response.body)["reviews"]

        # Yielding reviews until there are no more
        if reviews:
            for review in reviews:
                reviewItem = Review()

                reviewItem["id"] = review["id"]
                reviewItem["rating"] = review["rating"]
                reviewItem["title"] = review["title"]
                reviewItem["content"] = review.get("comment", None)
                reviewItem["date"] = review["submissionTime"]
                reviewItem["reviewer_name"] = review["reviewerName"]
                reviewItem["reviewer_location"] = review.get("reviewerLocation", None)
                reviewItem["verified_purchase"] = review["isVerifiedPurchaser"]
                reviewItem["product_id"] = response.request.meta["id"]

                yield reviewItem

            yield response.follow(
                url=f'https://www.bestbuy.ca/api/reviews/v2/products/{response.request.meta["id"]}/'
                f'reviews?source=all&lang=en-CA&pageSize=100&page={page + 1}&sortBy=relevancy',
                meta={"page": page + 1, "id": response.request.meta["id"]},
            )
