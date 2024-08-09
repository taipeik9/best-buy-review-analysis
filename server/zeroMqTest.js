const zmq = require("zeromq");

async function run() {
  var scraping = false;
  const socket = new zmq.Request();
  socket.connect("tcp://127.0.0.1:4242");

  await socket.send(JSON.stringify({ query: "computers" }));

  do {
    const [result] = await socket.receive();
    const res = JSON.parse(result);
    scraping = res.scraping;

    console.log(res.message);
  } while (scraping);
}

run();
