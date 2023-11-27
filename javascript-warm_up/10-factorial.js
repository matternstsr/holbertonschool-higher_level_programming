#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n)) { return 1; }

  if (n === 0) { return 1; }

  return n * factorial(n - 1);
};

const arg = process.argv[2];

const n = parseInt(arg);

const result = factorial(n);

console.log(`Factorial of ${args} is: ${result}`);
