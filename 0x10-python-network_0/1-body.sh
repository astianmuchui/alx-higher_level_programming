#!/bin/bash
# Will display the body of a response only if 200 is the response code
curl -s "%{http_code}" -o response.txt "$@" && [ "$(tail -n 1 response.txt)" == "200" ] && curl --location "$@" --request GET -w
