#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Geting the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Checking if both arguments are provided
if (!url || !filePath) { console.error('Usage: ./5-request_store.js <URL> <file-path>'); process.exit(1); }

// Making a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) { console.error(error); process.exit(1); }

  // Writing the contents to the specified file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) { console.error(err); process.exit(1); }

    console.log('body response written to {filePath}');
  });
});
