# Definición de la clase "Perro"
class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
    
    def ladrar(self):
        print("¡Guau! ¡Guau!")
    
    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("Raza:", self.__raza)
        print("Edad:", self.__edad)

# Creación de un objeto a partir de la clase "Perro"
mi_perro = Perro("Firulais", "Golden Retriever", 3)

# Llamada al método "ladrar" del objeto creado
mi_perro.ladrar()

# Llamada al método "mostrar_info" del objeto creado
mi_perro.mostrar_info()
