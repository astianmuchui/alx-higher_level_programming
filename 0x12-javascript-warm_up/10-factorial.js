#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];

function factorial (a) {
  let b = 1;
  while (a > 1) {
    b *= a;
    a--;
  }
  return (b);
}

if (isNaN(parseInt(arg))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(arg)));
}
