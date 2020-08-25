#!/usr/bin/python3
"""Sends a POST request to http://IP:5000/search_user with letter as a parameter"""

import sys
import requests


if __name__ == "__main__":
    data = {"q": ""}
    if len(argv) > 1:
        data['q'] = sys.argv[1]
    url = requests.get("http://0.0.0.0:5000/search_user")
    if "json" not in url.headers.get("content-type"):
        print("Not a valid JSON")
    else:
        if url.json():
            print("[{}] {}".format(url.json().get("id"), url.json().get("name")))
        else:
            print("No result")
