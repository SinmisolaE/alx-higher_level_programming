#!/usr/bin/node

let x = process.argv[2];
let i = 0;

if (isNaN(x) || x === undefined) {
  console.log("Missing size");
} else {
  while (i < parseInt(x)) {
    console.log('X'.repeat(x));
    i++;
  }
