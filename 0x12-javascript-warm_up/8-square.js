#!/usr/bin/node

const [,, arg1] = process.argv;
const size = parseInt(arg1);

if (!isNaN(size)) {
  for (let row = 0; row < size; row++) {
    let square = '';
    for (let col = 0; col < size; col++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
