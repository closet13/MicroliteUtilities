import requests
import char_creator as cc


def send_char():
    zed = cc.Character()
    zed.char_gen()
    data = zed.json_output()
    return requests.post(data=data, url='http://127.0.0.1:5001')

