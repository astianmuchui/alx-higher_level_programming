#!/usr/bin/node

const InitSquare = require('./5-square');

class Square extends InitSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
