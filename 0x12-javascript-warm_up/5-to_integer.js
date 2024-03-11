#!/usr/bin/node

if (isNaN(process.argv[1]) || process.argv[1] === undefined)
	console.log("Not a number");
else
	console.log("My number: " + parseInt(process.argv[1]));
