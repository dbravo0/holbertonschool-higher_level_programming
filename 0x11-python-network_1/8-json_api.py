#!/usr/bin/python3
"""Sends a POST request to IP:5000/search_user with letter as a parameter"""

import sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        data = {"q": argv[1][0]}
    else:
        data = None
    req = requests.post(url, data=data)
    try:
        j = req.json()
        if not j:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
    except ValueError:
        print("Not a valid JSON")
