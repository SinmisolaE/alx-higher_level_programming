#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error.message);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((movie) => {
      movie.characters.forEach((charact) => {
        if (charact.includes(18)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
