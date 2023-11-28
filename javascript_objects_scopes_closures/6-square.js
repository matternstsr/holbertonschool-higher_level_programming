#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  constructor (size) { super(size); }

  charPrint (c) {
    const whichPrint = c || 'X';
    for (let i = 0; i < this.height; i++) { console.log(whichprint.repeat(this.width)); }
  }
}
module.exports = Square;
