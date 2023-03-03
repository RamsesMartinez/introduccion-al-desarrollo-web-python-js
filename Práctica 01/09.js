const fs = require('fs');
const archivo = process.argv[2];
fs.readFile(archivo, 'utf-8', (error, contenido) => {
  if (error) {
    console.log('Error al leer el archivo.');
  } else {
    const objeto = JSON.parse(contenido);
    console.log(objeto);
  }
});
