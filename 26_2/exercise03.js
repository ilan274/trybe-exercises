const fs = require('fs');
const readline = require('readline');
const path = require('path');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const readFileCallback = () => {
  rl.question('Please enter a file name [callback]: ', fileName => {
    fs.readFile(path.join(__dirname, fileName), (err, data) => {
      if (err) throw new Error(`Something went wrong: ${err.code}`);
      return (
        console.log(`----\n${data.toString('utf8')}\n----`),
        console.log(`File size: ${data.byteLength} bytes`)
      );
    });
    rl.close();
  });
};
readFileCallback();