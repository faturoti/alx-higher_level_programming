#!/bin/bash
# The code to etract the status code from HTTP response
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
