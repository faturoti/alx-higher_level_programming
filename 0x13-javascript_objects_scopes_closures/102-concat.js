#!/usr/bin/node
const fs = require('fs');
const one = fs.readFileSync(process.argv[2], 'utf8');
const two = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], one + two);
