#!/usr/bin/node

let x;
x = process.argv[2];

if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
