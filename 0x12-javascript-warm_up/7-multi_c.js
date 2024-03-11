#!/usr/bin/node

let x = process.argv[2];

if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  x = Number(x);
  for (let i = 0; i < (x); i++) {
    console.log('C is fun');
  }
}
