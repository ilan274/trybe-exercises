const os = require('os');

setInterval(() => {
  console.log(((os.totalmem() - os.freemem()) / 1024 / 1024 / 1024).toFixed(2));
}, 2000);
