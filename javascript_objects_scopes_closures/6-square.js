#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  charPrint (c) {
    const whichPrint = c || 'X';
    for (let i = 0; i < this.height; i++) { console.log(whichPrint.repeat(this.width)); }
  }
}
module.exports = Square;
// the constructor in the Square class is considered useless.
// The reason for this suggestion might be that the constructor in Square is doing the same
// thing as the constructor in the parent class, and it doesn't have any additional functionality.
// omit the constructor in the Square class if it doesn't have additional logic.
