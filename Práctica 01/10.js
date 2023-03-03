const request = require('request');
const sitioWeb = process.argv[2];
request(sitioWeb, (error, respuesta, cuerpo) => {
  if (error) {
    console.log('Error al hacer la solicitud.');
  } else {
    console.log(cuerpo);
  }
});
