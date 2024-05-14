#!/usr/bin/python3

"""This is a script that fetches the url using url lib"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
