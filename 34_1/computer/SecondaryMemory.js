const fs = require('fs');

const DISK_PATH = './disk';

class SecondaryMemory {
  load(value) {
    const disk = fs.readdirSync(DISK_PATH);

    const nextFileName = `${DISK_PATH}/cel${disk.length}`;

    fs.writeFileSync(nextFileName, value);
  }

  get(index) {
    const fileName = `${DISK_PATH}/cel${index}`;

    const fs = require('fs');

    try {
      const data = fs.readFileSync(fileName, 'utf8');
      console.log('Dado lido:', parseFloat(data));
    } catch (err) {
      console.error('Erro ao ler o arquivo,', err);
    }
  }

  clean() {
    fs.rmdirSync(DISK_PATH, { recursive: true });
    fs.mkdirSync(DISK_PATH);
  }
}

module.exports = SecondaryMemory;
