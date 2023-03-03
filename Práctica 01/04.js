const fs = require('fs');
const archivo = process.argv[2];
const contenido = fs.readFileSync(archivo, 'utf-8');
console.log(contenido);
