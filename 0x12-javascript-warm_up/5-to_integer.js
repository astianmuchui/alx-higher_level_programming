#!/usr/bin/node
const process = require('process');
const arg = process.argv;

if (parseInt(arg[2])) {
  console.log('My Number: ' + parseInt(arg[2]));
} else {
  console.log('Not a number');
}
