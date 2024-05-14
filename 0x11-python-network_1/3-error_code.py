#!/usr/bin/python3

"""This is to display error from a site
-  The first Argument is the url
-  The responce is handle for error
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as req:
            print(req.read().decode('UTF-8'))
    except error.HTTPErrror as err:
        print('Error code:', err.code)
