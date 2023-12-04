const filePath = process.argv[2];

// Checking if a file path is there
if (!filePath) { console.error('Usage: node 0-readme.js <file-path>'); process.exit(1); }

// Reading the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => { if (err) { console.error(err); } else { console.log(data); } });
