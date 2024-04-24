#!/usr/bin/node
// read from file

const contnt = require('fs');
contnt.readFile(process.argv[2], 'utf8', function (error, data) {
  console.log(error || data);
});
