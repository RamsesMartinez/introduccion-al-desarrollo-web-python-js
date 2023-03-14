# Definición de la clase "Gato"
class Gato:
    # Definición del atributo "color"
    color = "Negro"
    
    # Definición del método "maullar"
    def maullar(self):
        print("Miau! Miau!")
    
# Creación de un objeto a partir de la clase "Gato"
mi_gato = Gato()

# Acceso al atributo "color" del objeto
print(mi_gato.color) # Imprime "Negro"

# Llamada al método "maullar" del objeto
mi_gato.maullar() # Imprime "Miau! Miau!"
