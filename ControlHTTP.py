import requests
from flask import Flask, json, request

app = Flask(__name__)


@app.route("/char")
def char_signal():
    if request.method == "GET":
        print("making request")
        char = requests.get(url='http://127.0.0.1:5001/char')
    elif request.method == "POST":
        char = request.data
        print("saving")
        print(str(char))
        with open("out.txt", 'w') as temp:
            temp.write(str(char))
    return "yay"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5002)
