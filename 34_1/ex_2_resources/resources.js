/* eslint-disable max-len */
/* A plataforma que estamos utilizando, por exemplo: linux , win32 , darwin , etc., a arquitetura, por exemplo, x32 ou x64 , e a versão (release). Para isso utilize o módulo os do NodeJS
Adicione o código para exibir a quantidade de cores da sua CPU e o modelo e a velocidade em gigahertz - GHz de cada um (utilize o valor vindo em speed e faça a conversão 😎).
Exiba também a quantidade total de memória RAM disponível em sua máquina em gigabytes - GB (faça a conversão também 😉).
 */
const os = require('os');

console.log(`Plataforma: ${os.platform()}`);
console.log(`Arquitetura: ${os.arch()}`);
console.log(`Versão(release): ${os.release()}`);

console.log(os.cpus().length);
console.log(`Total mem: ${(os.totalmem() / 1024 / 1024 / 1024).toFixed(2)}`);
os.cpus().forEach((core, i) => {
  console.log(`Core ${i + 1}: ${core.model} - Speed:${parseFloat(core.speed / 1000).toPrecision(2)}`);
});
