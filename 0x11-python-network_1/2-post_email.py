#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode("ascii")
    with urllib.request.urlopen(argv[1], data) as page:
        print(page.read().decode('utf-8'))
