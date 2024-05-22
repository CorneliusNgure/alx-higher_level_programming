#!/usr/bin/python3
"""Uses GitHub API to display the user's id using Basic Authentication.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, token)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(None)
