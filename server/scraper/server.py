import json

import zmq

from services.crawl import run_scraper

if __name__ == "__main__":
    query = None
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    socket.bind("tcp://127.0.0.1:4242")
    open = True
    print("Socket open and listening on port: 4242")

    while open:
        payload = socket.recv_json()
        print(f"Recieved request: {payload}")
        try:
            query = payload["query"].strip()
        except KeyError:
            socket.send_string(
                json.dumps({"message": "Error: Must provide Query", "scraping": True})
            )

        if query:
            socket.send_string(
                json.dumps({"message": "Starting Scraping", "scraping": True})
            )
            run_scraper(query, socket)

            socket.recv_json()
            socket.send_string(json.dumps({"message": "Finished!", "scraping": False}))

    # socket.close()
    # context.term()
