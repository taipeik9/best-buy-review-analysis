# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Class to represent Product Item
class Product(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    short_description = scrapy.Field()
    avg_rating = scrapy.Field()
    rating_count = scrapy.Field()
    regular_price = scrapy.Field()
    sale_price = scrapy.Field()
    category_name = scrapy.Field()


# Class to represent Review Item
class Review(scrapy.Item):
    id = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    reviewer_name = scrapy.Field()
    reviewer_location = scrapy.Field()
    verified_purchase = scrapy.Field()
    product_id = scrapy.Field()
