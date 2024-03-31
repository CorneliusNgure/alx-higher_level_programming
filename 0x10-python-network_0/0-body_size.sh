#!/bin/bash
# Displays the size of the body of a HTTP request response.
curl -s "$1" | wc -c
