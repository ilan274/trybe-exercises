const fs = require('fs');
const path = require('path');

const startTime = Date.now();
const fileDone = fs.readFileSync(
  path.join(__dirname, 'asd.txt')
);
const timeToRead = Date.now() - startTime;
console.log(`asd.txt read in ${timeToRead}ms. Total bytes: ${fileDone.byteLength}`);

const startTime2 = Date.now();
const fileDone2 = fs.readFileSync(
  path.join(__dirname, 'asd2.txt')
);
const timeToRead2 = Date.now() - startTime2;
console.log(`asd2.txt read in ${timeToRead2}ms. Total bytes: ${fileDone2.byteLength}`);
