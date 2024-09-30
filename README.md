# Best Buy Review Scraper Web Application

This is a best buy review scraper web application. Currently in version 0.1!

(Demo is pending)
<img width="1209" alt="home" src="https://github.com/user-attachments/assets/0958fc4f-9c59-4725-ac7e-c44073a06362">

With this web app you can search query whatever you want on Best Buy and collect all of the resulting products and their review data.

I used NextJS for the front end, FastAPI for the back end and SQLite for the database. This is my first time working with FastAPI, NextJS and Typescript. So, any feedback is welcome. I decided to go with FastAPI, even though I am unfamiliar with it because my webscraper was done in Python using the Scrapy package. I tried going with a NodeJS express API and having it make calls to the Python webscraper but in the end I decided to learn something new to prevent overcomplicating the issue.

### Current Development and Looking Forward
This project has been so much fun. I am excited to expand on it. Right now you can:
- query anything on Best Buy and collect all of the reviews for related products
- view all of the reviews and products which were scraped
- view all of your scraping sessions
- interact with the scraper and database with an easy-to-use NextJS front-end
- spin up the API yourself with `docker compose up --build` in the server directory.

Looking forward, these are the next tasks I want to tackle:
- sessions to products to reviews should be a many-to-many relationship, they are currently many-to-one. This involves a database redesign, so it will no doubt be inconvenient :(... but better than trying to solve the issue later
- searching through reviews and products on the front end
- sorting products and reviews (sorting reviews in the table)
- downloading products and reviews in csv or json format
- improve error handling (right now it is basically non-existent on the front-end)
- cleaning up the front end so that it looks better and feels more intuitive
- Dockerize the entire project so that the webapp and server run from one docker instruction.
- (long goal) performing insights on the data directly on the site, avoiding the need for a download. Different kinds of analysis can be done on the reviews, especially because this is a Python back-end I think it will flow nicely. Sentiment analysis, keyword extraction, and comparisons between products based on these metrics could be done on the reviews. And whatever else I think of in the process.

Feel free to message me if you have any questions about this project :).

### Screenshots of other pages:

Products Page:
<img width="1174" alt="products" src="https://github.com/user-attachments/assets/8e7fb0a9-bc75-46e5-aa59-183f3ca05135">

Reviews for Product:
<img width="1187" alt="reviews-for-product" src="https://github.com/user-attachments/assets/e7bcab31-bb1b-4cdf-a420-4643936ead4f">

Review Details:
<img width="1172" alt="review-details" src="https://github.com/user-attachments/assets/e62558fd-4a6c-4223-b68d-8d7e3f25c639">

