const http = require('http');
const servidor = http.createServer((req, res) => {
  res.end('Hola, mundo!');
});
servidor.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000.');
});
