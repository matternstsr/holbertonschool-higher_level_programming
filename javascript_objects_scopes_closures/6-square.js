#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  charPrint (c) {
    const whichPrint = c || 'X';
    for (let i = 0; i < this.height; i++) { console.log(whichPrint.repeat(this.width)); }
  }
}
module.exports = Square;
