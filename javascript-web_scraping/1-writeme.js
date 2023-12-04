#!/usr/bin/node
const fs = require('fs');

// Get file path and string from command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Check if both arguments are provided
if (!filePath || !contentToWrite) {
  console.error('Usage: node 1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

// Write content to the file
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) { console.error(err); }
});
