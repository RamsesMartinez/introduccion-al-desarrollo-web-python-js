const http = require('http');
const fs = require('fs');
const servidor = http.createServer((req, res) => {
  if (req.method === 'GET') {
    fs.readFile('formulario.html', 'utf-8', (error, contenido) => {
      if (error) {
        res.end('Error al leer el archivo.');
      } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(contenido);
      }
    });
  } else if (req.method === 'POST') {
    let datos = '';
    req.on('data', (chunk) => {
      datos += chunk;
    });
    req.on('end', () => {
      fs.writeFile('datos.txt', datos, (error) => {
        if (error) {
          res.end('Error al guardar los datos.');
        } else {
          res.writeHead(200, {'Content-Type': 'text/plain'});
          res.end('Datos guardados correctamente.');
        }
      });
    });
  } else {
    res.end('Método no permitido.');
  }
});
servidor.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000.');
});
