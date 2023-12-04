const request = require('request');
const url = process.argv[2];

// Check if a URL
if (!url) { console.error('Usage: node 2-statuscode.js <URL>'); process.exit(1);}

// Make a request and check for errors??
request(url, (error, response) => { if (error) { console.error(`Error: {error.message}`); process.exit(1);}

  // Print the status code to the answer
  console.log(`code: {response.statusCode}`);});
