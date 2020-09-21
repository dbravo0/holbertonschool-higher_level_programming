#!/usr/bin/node
const Square2 = require('./5-square');

module.exports = class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
};
