#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [,, arg1, arg2] = process.argv;
const FirstNum = parseInt(arg1);
const SecondNum = parseInt(arg2);

console.log(add(FirstNum, SecondNum));
