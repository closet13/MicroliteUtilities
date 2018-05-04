import requests
import char_creator as cc
from flask import Flask, json, request

app = Flask(__name__)


@app.route("/char")
def char_signal():
    char: object
    if request.method == "GET":
        print("making request")
        char = requests.get(url='http://127.0.0.1:5001/char')
    else:

    return "yay"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5002)
