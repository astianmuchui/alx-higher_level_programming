#!/usr/bin/node
const process = require('process');
const arg = process.argv;

if (arg.length < 4) {
  console.log(0);
} else {
  const myarr = arg.slice().sort((a, b) => b - a);
  console.log(myarr[3]);
}
