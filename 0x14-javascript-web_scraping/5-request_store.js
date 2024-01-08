#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
