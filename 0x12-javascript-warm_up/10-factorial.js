#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];

function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

if (isNaN(parseInt(arg))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(arg)));
}
