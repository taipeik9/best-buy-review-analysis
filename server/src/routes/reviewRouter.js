const express = require("express");
const router = express.Router();

const {
  getAllReviews,
  createNewReviews,
} = require("../controllers/reviewController");

router.get("/", getAllReviews);

router.post("/", createNewReviews);

module.exports = router;
