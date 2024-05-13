#!/usr/bin/python3

"""This is a script that fetches the url using url lib"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        res = r.read()

        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))
