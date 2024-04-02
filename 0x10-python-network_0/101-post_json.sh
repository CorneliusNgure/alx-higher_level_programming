#!/bin/bash
# Sends a JSON post request to a give URL and displays body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
