#!/bin/bash
# Will display the body of a response only if 200 is the response
curl -s -o response.txt "$1" && [ "$(curl -s -w "%{http_code}" "$1")" == "200" ] ; curl --location --request GET "$1"
