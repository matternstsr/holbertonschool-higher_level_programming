#!/usr/bin/node
const fs = require('fs');

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Check if both file path and content are provided
if (!filePath || !contentToWrite) {
  console.error('Usage: node 1-writeme.js <file-path> <content-to-write>');
  process.exit(1);
}

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  // Check for errors during writing
  if (error) {
    console.error(error);
    process.exit(1);
  }

  console.log(`[Got]\nContent has been written to ${filePath}`);
});
