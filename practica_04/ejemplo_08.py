# Definición de la clase "Libro" 
class Libro: 
    def __init__(self, titulo, autor, anio_publicacion, num_paginas): 
        self.__titulo = titulo 
        self.__autor = autor 
        self.__anio_publicacion = anio_publicacion 
        self.__num_paginas = num_paginas 
   
    def obtener_informacion(self): 
        print(f"El libro '{self.__titulo}' de {self.__autor} fue publicado en el año {self.__anio_publicacion} y tiene {self.__num_paginas} páginas.") 

# Creación de un objeto a partir de la clase "Libro" 
mi_libro = Libro("El nombre del viento", "Patrick Rothfuss", 2007, 662) 

# Llamada al método "obtener_informacion" del objeto 
mi_libro.obtener_informacion()


