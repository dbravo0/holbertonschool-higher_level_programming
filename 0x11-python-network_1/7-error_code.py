#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""

import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    if resp.status_code > 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(response.text)
