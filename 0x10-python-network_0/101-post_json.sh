#!/bin/bash
# This is the code to send post in json forma
curl -s "$1" -H "Content-Type: application/json" -d "$(cat "$2")"
