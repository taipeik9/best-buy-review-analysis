// Initializing and creating SQL Database

const sqlite = require("sqlite3").verbose();

const db = new sqlite.Database("bestbuy.db", sqlite.OPEN_READWRITE, (err) => {
  if (err) return console.log(err);
});

const drop = `DROP TABLE IF EXISTS reviews, sessions, products`;

const createTable = `
  CREATE TABLE reviews (
    review_id 
  )
`;
