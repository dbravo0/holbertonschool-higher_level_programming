#!/bin/bash
# Makes a request to IP:5000/catch_me that causes the server to respond with a message
curl -sLH -X "PUT" "X-HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
