#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the response.
If the HTTP status code is >= 400,
+ prints an error message with the status code.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
