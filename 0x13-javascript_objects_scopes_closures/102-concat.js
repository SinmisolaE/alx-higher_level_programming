#!/usr/bin/node

const fs = require('fs');

const first = fs.readFileSync(process.argv[2]).toString();
const sec = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], first + sec);
