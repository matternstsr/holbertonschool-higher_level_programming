#!/usr/bin/node

const add = (a, b) => a + b;

const intone = parseInt(process.argv[2]);
const inttwo = parseInt(process.argv[3]);

if (!isNaN(intone) && Number.isInteger(intone) &&
    !isNaN(inttwo) && Number.isInteger(inttwo)) { console.log(add(intone, inttwo)); }
