#!/usr/bin/node

const args = process.argv.length - 2;

if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
