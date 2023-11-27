#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) { console.log('HBTN is undefined'); } else { const secondArg = process.argv[3] === 'undefined' ? 'undefined' : process.argv[3]; console.log(`${process.argv[2]} is ${secondArg}`); }
