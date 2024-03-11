#!/usr/bin/node

let x = process.argv[2];
let i = 0;

if (isNaN(x) || x === undefined) {
  console.log('Missing size');
} else {
  x = Number(x);
  while (i < (x)) {
    console.log('X'.repeat(x));
    i++;
  }
}
