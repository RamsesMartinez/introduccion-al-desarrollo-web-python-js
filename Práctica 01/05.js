const fs = require('fs');
const archivo = process.argv[2];
const mensaje = process.argv[3];
fs.writeFileSync(archivo, mensaje);
console.log('Archivo escrito correctamente.');
