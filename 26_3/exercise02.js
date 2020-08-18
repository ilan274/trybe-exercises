const fs = require('fs');
const path = require('path');

const startTime = Date.now();
fs.readFile(path.join(__dirname, 'asd.txt'), (err, data) => {
  if (err) throw new Error(`Something went wrong: ${err.code}`);
  const readTime = Date.now() - startTime;
  console.log(`asd.txt read in ${readTime}ms. Total bytes: ${data.byteLength}`);
});

const startTime2 = Date.now();
fs.readFile(path.join(__dirname, 'asd2.txt'), (err, data) => {
  if (err) throw new Error(`Something went wrong: ${err.code}`);
  const readTime2 = Date.now() - startTime2;
  console.log(`asd2.txt read in ${readTime2}ms. Total bytes: ${data.byteLength}`);
});
