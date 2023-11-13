#!/usr/bin/node
const process = require('process');
const arg = process.argv;

if (parseInt(arg[2])) {
  for (let i = 0; i < parseInt(arg[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
