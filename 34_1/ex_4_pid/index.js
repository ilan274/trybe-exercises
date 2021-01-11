const process = require('process');
const { exec } = require('child_process');
exec(`kill -9 ${2}`, (err, stdout, stderr) => {
  console.log();
});
// console.log(process.pid);
