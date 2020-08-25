#!/usr/bin/python3
"""Sends a POST request to IP:5000/search_user with letter as a parameter"""

import sys import argv
import requests


if __name__ == "__main__":
    data = {'q': ""}
    if len(argv) > 1:
        data['q'] = argv[1]
    url = requests.get("http://0.0.0.0:5000/search_user", data)
    if "json" not in url.headers.get("content-type"):
        print("Not a valid JSON")
    else:
        j = url.json()
        if not j:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
    except ValueError:
        print("Not a valid JSON")
