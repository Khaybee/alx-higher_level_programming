#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let indexI = 0; indexI < this.height; indexI++) {
      let txt = '';
      for (let indexJ = 0; indexJ < this.width; indexJ++) {
        txt += 'X';
      }
      console.log(txt);
    }
  }

  rotate () {
    const auxi = this.width;
    this.width = this.height;
    this.height = auxi;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
