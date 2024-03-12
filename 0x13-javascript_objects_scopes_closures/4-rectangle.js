#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w !== 0 && h !== 0 && w !< 0 && h !< 0) {
      this.width = w;
      this.height = h;
    }

  print() {
    for (let i = 0; i < h; i++) {
      console.log('X'.repeat(this.height);
    }
  }

  rotate() {
    let c = this.width;
    this.width = this.height;
    this.height = c;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}
