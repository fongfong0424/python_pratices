#!/usr/bin/python

import requests

def get_joke():
    url = "https://autumnfish.cn/api/joke"
    date = requests.get(url)
    return date.text

joke = get_joke()
print(joke)