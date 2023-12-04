#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Checking if the URL is provided
if (!url) { console.error('Usage: ./2-statuscode.js <URL>'); process.exit(1); }

// Making a get request to the specified URL
request.get(url, (error, response) => { if (error) { console.error(error); process.exit(1); }

  // Display the status code
  console.log('code:', response.statusCode); });
