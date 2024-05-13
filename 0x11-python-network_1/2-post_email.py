#!/usr/bin/python3

"""This is aprogram that send email to the wepage
- url is first parameter
- email is the second parameter
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
