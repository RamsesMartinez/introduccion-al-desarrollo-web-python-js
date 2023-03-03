const fs = require('fs');

const mensaje = "Este es un mensaje que se escribirá en el archivo.";

fs.writeFile('archivo.txt', mensaje, err => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('El archivo ha sido escrito satisfactoriamente.');
});
