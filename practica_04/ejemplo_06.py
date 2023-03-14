# Definición de la clase "Animal"
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass

# Definición de la clase "Perro", que hereda de la clase "Animal"
class Perro(Animal):
    def hablar(self):
        print("El perro está ladrando")

# Definición de la clase "Gato", que hereda de la clase "Animal"
class Gato(Animal):
    def hablar(self):
        print("El gato está maullando")

# Creación de una lista de objetos de la clase "Animal"
animales = [Perro("Firulais"), Gato("Garfield")]

# Llamada al método "hablar" de cada objeto en la lista
for animal in animales:
    animal.hablar()
