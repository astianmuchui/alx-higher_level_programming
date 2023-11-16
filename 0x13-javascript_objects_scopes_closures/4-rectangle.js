#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const rect = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }

  rotate () {
    const tempw = this.width;
    const temph = this.height;
    this.width = temph;
    this.height = tempw;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
