#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const character of JSON.parse(body).characters) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
