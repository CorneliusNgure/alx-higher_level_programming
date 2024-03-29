#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const [,, arg1] = process.argv;
const num = parseInt(arg1);

console.log(factorial(num));
