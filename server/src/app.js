const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const reviewRoutes = require("./routes/reviewRouter");

const PORT = 3000;
const app = express();

app.use(cors());
app.use(bodyParser.json());

app.use("/reviews", reviewRoutes);

app.listen(PORT, () => {
  console.log(`Server listening on PORT: ${PORT}`);
});
