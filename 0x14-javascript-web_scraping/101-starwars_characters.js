#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    for (const character of content.characters){
      request.get(character, function (error, resp, body1) {
        if (error) {
          console.log(error);
        } else {
          const cont = JSON.parse(body1);
          console.log(cont.name);
        }
      });
    }
  }
});
