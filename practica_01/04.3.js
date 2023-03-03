// Crea un script de Node.js que lea un archivo de texto 
// y lo imprima en la consola.

const fs = require('fs');
const archivo = process.argv[2];
const contenido = fs.readFileSync(archivo, 'utf-8');
console.log(contenido);
