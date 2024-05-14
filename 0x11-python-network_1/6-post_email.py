#!/usr/bin/python3

"""To post an email to a specified url
-  url is first argument
-  email is second argument
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    v = {"email", sys.argv[2]}

    req = requests.post(url, data=v)
    print(req.text)
