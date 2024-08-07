import sqlite3
import json


# Inserting products into SQL db
def upload_products(cursor, filename):
    with open(filename) as f:
        products = json.load(f)

    for product in products:
        cursor.execute(
            "INSERT INTO products (id, title, short_description, avg_rating, rating_count, regular_price, sale_price, category_name)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?) ",
            (
                product.get("id", None),
                product.get("title", None),
                product.get("short_description", None),
                product.get("avg_rating", None),
                product.get("rating_count", None),
                product.get("regular_price", None),
                product.get("sale_price", None),
                product.get("category_name", None),
            ),
        )


# Inserting reviews into SQL db
def upload_reviews(cursor, filename):
    with open(filename) as f:
        reviews = json.load(f)

    for review in reviews:
        cursor.execute(
            "INSERT INTO reviews (id, rating, title, content, date, reviewer_name, reviewer_location, verified_purchase, product_id)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ",
            (
                review.get("id", None),
                review.get("rating", None),
                review.get("title", None),
                review.get("content", None),
                review.get("date", None),
                review.get("reviewer_name", None),
                review.get("reviewer_location", None),
                review.get("verified_purchase", None),
                review.get("product_id", None),
            ),
        )


# Function to connect to SQL db then insert both products and reviews, commit and close
def upload_products_and_reviews(products_filename, reviews_filename):
    con = sqlite3.connect("../db/bestbuy.db")
    cursor = con.cursor()
    upload_products(cursor, products_filename)
    upload_reviews(cursor, reviews_filename)
    con.commit()
    con.close()
