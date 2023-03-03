// Crea un script de Node.js que reciba dos números de línea de
// comandos e imprima la suma de esos dos números en la consola.

const numero1 = Number(process.argv[2]);
const numero2 = Number(process.argv[3]);
const suma = numero1 + numero2;
console.log(suma);
