#!/bin/bash
# Sends a request to an URL and displays the size of the body of the response
curl -Is "$1" | grep "Content-Length" | cut -d " " -f 2
