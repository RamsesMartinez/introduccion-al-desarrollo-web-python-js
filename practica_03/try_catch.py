try: 
    # Bloque de código que puede generar una excepción 
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: ")) 
    resultado = num1 / num2 
    print(f"El resultado de la división es: {resultado}") 
except ValueError: 
    # Bloque de código que se ejecuta si se produce una excepción ValueError   
    print("Error: Se deben ingresar números enteros.") 
except ZeroDivisionError: 
    # Bloque de código que se ejecuta si se produce una excepción
    # ZeroDivisionError 
    print("Error: No se puede dividir por cero.")


