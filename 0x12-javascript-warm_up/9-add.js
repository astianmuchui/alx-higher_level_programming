#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  return (a + b);
}

if (parseInt(arg) && parseInt(arg2)) {
  console.log(add(parseInt(arg), parseInt(arg2)));
} else {
  console.log(NaN);
}
