from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def get_char():
    """
    time to think. Im over-complicating things as usual. There only needs to be 1 server, the core server, which will
    answer and make requests, as well as forward data to and fro. The player main loop will make continuous requests
    which means the oly complex part will be in encoding the json so the right header is attached, as well as correctly
    coordinating between the player and GM. This needs more thought and a whiteboard
    :return:
    """
    return ascii("wenis")


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)
