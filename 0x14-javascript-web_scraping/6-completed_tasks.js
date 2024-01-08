#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const iscomplete = {};

    for (const todo of todos) {
      if (todo.iscomplete && iscomplete[todo.userId] === undefined) {
        iscomplete[todo.userId] = 1;
      } else if (todo.iscomplete) {
        iscomplete[todo.userId] += 1;
      }
    }

    console.log(iscomplete);
  }
});
