#!/usr/bin/node

function factorial(x)
{
	if (isNaN(x) || x === undefined)
		return (1);
	return (x * factorial(x - 1));
}

factorial(process.argv[1]);
