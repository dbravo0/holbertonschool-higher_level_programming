#!/usr/bin/python3
"""Takes your Github credentials (username and password) and display your id"""

import requests
from sys import argv


if __name__ == "__main__":
    url = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    try:
        print(url.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
