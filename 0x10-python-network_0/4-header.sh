#!/bin/bash
# takes a URL as an argument, sends a GET request to URL and displays response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
