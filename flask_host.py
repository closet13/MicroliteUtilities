from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

clients = ["http://127.0.0.1:5000/char"]
controller = "http://127.0.0.1:5002"


@app.route('/char', methods=["POST", "GET"])
def get_char():
    """
    time to think. Im over-complicating things as usual. There only needs to be 1 server, the core server, which will
    answer and make requests, as well as forward data to and fro. The player main loop will make continuous requests
    which means the oly complex part will be in encoding the json so the right header is attached, as well as correctly
    coordinating between the player and GM. This needs more thought and a whiteboard
    :return:
    """
    if request.method == "POST":
        with open("test.txt", 'r') as temp:
            char = temp.read()
        print("returning data")
        requests.post(data=char, url=controller+'/char')
    elif request.method == "GET":
        print("getting data")
        char = requests.get(url=clients[0])
        with open("test.txt", 'w') as temp:
            temp.write(char.text)
    return "yay"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)
