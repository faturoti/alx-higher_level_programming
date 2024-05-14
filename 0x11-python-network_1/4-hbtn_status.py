#!/usr/bin/python3

"""This is a script that fetches the url using url lib"""

if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(r.__class__))
    print("\t- content: {}".format(r.text))
