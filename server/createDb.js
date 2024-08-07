// Initializing and creating SQL Database

const sqlite = require("sqlite3").verbose();

const db = new sqlite.Database(
  "db/bestbuy.db",
  sqlite.OPEN_READWRITE,
  (err) => {
    if (err) return console.log(err);
  }
);

const createProducts = `
  CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    short_description TEXT DEFAULT NULL,
    avg_rating FLOAT NOT NULL,
    rating_count INTEGER NOT NULL,
    regular_price FLOAT NOT NULL,
    sale_price FLOAT NOT NULL,
    category_name TEXT
  )
`;

const createReviews = `
  CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    rating INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT DEFAULT NULL,
    date TEXT NOT NULL,
    reviewer_name TEXT NOT NULL,
    reviewer_location TEXT DEFAULT NULL,
    verified_purchase BOOLEAN NOT NULL,
    product_id INTEGER,
    CONSTRAINT FK_productid FOREIGN KEY (product_id) REFERENCES products(id)
  )
`;

db.serialize(() => {
  db.run(`DROP TABLE IF EXISTS reviews`)
    .run(`DROP TABLE IF EXISTS products`)
    .run(createProducts)
    .run(createReviews);
});
