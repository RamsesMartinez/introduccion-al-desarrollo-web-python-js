# Definición de la clase "Persona"
class Persona:
    # Constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        print("Se ha creado una persona llamada", self.nombre)
    
    # Destructor de la clase
    def __del__(self):
        print("Se ha eliminado la persona llamada", self.nombre)

# Creación de un objeto a partir de la clase "Persona"
mi_persona = Persona("Juan")

# Eliminación del objeto creado
del mi_persona
