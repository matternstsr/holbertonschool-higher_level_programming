#!/usr/bin/node

const times = parseInt(process.argv[2]);

if (!isNaN(times) && Number.isInteger(times)) {
  for (let i = 0; i < times; i++) {
    console.log("c is fun");
  }
} else {
  console.log("missing number of occurrences");
}