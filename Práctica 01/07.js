const http = require('http');
const fs = require('fs');
const servidor = http.createServer((req, res) => {
  if (req.url === '/') {
    fs.readFile('index.html', 'utf-8', (error, contenido) => {
      if (error) {
        res.end('Error al leer el archivo.');
      } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(contenido);
      }
    });
  } else if (req.url === '/estilos.css') {
    fs.readFile('estilos.css', 'utf-8', (error, contenido) => {
      if (error) {
        res.end('Error al leer el archivo.');
      } else {
        res.writeHead(200, {'Content-Type': 'text/css'});
        res.end(contenido);
      }
    });
  } else {
    res.end('Página no encontrada.');
  }
});
servidor.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000.');
});
