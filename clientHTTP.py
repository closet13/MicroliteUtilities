import requests
import char_creator as cc
from flask import Flask, json, request

app = Flask(__name__)


@app.route("/char", methods=["GET", "POST"])
def send_char():
    zed = cc.Character()
    zed.char_gen()
    data = zed.json_output()
    print("responding to request")
    requests.post(data=data, url='http://127.0.0.1:5001/char')
    return "yay"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
