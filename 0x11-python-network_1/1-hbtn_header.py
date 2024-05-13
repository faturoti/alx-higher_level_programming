#!/usr/bin/python3

"""This is the code to get the ID of the Url loaded
-  X-Request-IdX-Request-Id"""

import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get('X-Request-Id'))
