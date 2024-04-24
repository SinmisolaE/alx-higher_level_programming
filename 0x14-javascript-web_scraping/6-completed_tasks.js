#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const taskComplete = {};
    content.forEach((task) => {
      if (task.completed) {
        if (!taskComplete[task.userId]) {
          taskComplete[task.userId] = 1;
        } else {
          taskComplete[task.userId]++;
        }
      }
    });
    console.log(taskComplete);
  }
});
