#!/usr/bin/node

exports.esrever = function (list) {
  let length = list.length;
  for (let i = 0; i < lenght: i++) {
    let c = list[i];
    list[i] = list[length - 1];
    list[length - 1] = c;
    length--;
  }
};
