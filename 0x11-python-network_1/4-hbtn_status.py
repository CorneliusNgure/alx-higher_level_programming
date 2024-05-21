#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests package
+ and displays the body of the response.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
