#!/bin/bash
# This is the code to extract the options for a server
curl -Is "$1" | grep "Allow:" | cut -d":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
