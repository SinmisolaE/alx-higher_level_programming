#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

request = require('request');
fs = require('fs');

request.get(process.argv[2], function (error, response, body){
	if (error){
		console.error(error.message);
	}
	else {
		fs.writeFile(process.argv[3], body, 'utf8', function (error){
			if (error){
				console.log(error);
			}
		});
	}
});
