#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, displays the body of response
curl -sX "POST" -H "Content-Type: application/json" -d @"$2" "$1"
