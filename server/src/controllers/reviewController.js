const getAllReviews = (req, res) => {
  res.status(200).json({ message: "Handling get req" });
};

const scrapeReviews = (query) => {
  const { spawn } = require("child_process");
  const pythonProcess = spawn("python", ["../../scraper/crawl.py"]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(data.toString());
  });
};

const createNewReviews = (req, res) => {
  if (Object.keys(req.body).length === 0)
    return res
      .status(400)
      .json({ success: false, message: "Request body is required" });

  scrapeReviews("computers");

  return res.status(200).json({ success: true });
};

module.exports = { getAllReviews, createNewReviews };
