#!/usr/bin/python3
"""Uses Github API to list the 10 most recent commits"""

import requests
from sys import argv


if __name__ == '__main__':
    url = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1]))
    for commit in url.json()[:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
