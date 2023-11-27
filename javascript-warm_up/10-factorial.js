#!/usr/bin/node

function factorial (a) {
  if (a < 0) { return 'Undefined'; } else if (isNaN(a) || a === 0 || a === 1) { return 1; } else { return a * factorial(a - 1); }
}

const arg = process.argv[2];
const n = parseInt(arg);
const result = factorial(n);

console.log(result.toString());
