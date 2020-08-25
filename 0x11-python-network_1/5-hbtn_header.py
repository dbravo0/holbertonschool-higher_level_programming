#!/usr/bin/python3
"""Sends a request to an URL and displays the value of variable X-Request-Id"""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
