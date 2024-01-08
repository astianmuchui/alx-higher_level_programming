#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fs.WriteStream(file, content, (err) => {
  if (err) throw err;
});
