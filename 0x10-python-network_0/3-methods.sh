#!/bin/bash
# Will display all methods that a server accepts
curl -sI -X OPTIONS "%{allowed}" "$@" | grep -i Allow
