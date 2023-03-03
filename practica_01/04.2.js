const readline = require("readline");
const fs = require("fs");
const NOMBRE_ARCHIVO = "archivo.txt";

let lector = readline.createInterface({
    input: fs.createReadStream(NOMBRE_ARCHIVO)
});

lector.on("line", linea => {
    console.log("Tenemos una línea:", linea);
});
