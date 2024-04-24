#!/usr/bin/node
// writes into a file

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (error) {
  if (error) {
    console.log(error.message);
  }
});
