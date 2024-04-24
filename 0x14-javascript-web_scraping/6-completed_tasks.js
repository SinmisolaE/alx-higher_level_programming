#!/usr/bin/node
//computes the number of tasks completed by user id.

request = require('request');

request.get(process.argv[2], function (error, response, body){
	if (error){
		console.log(error);
	}
	else {
		const content = JSON.parse(body);
		const task_complete = {};
		content.forEach((task) => {
			if (task.completed) {
				if (!task_complete[task.userId]){
					task_complete[task.userId] = 1;
				}
				else {
					task_complete[task.userId]++;
				}
			}
		});
		console.log(task_complete);
	}
});
