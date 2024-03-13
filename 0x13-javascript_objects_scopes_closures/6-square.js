#!/usr/bin/node

const Square = require('./5-square.js');

class Square extends Square {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < super(size); i++) {
      console.log(c.repeat(super(size)));
    }
}
module.exports = Square;
