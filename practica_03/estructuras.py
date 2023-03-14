import random

numero_secreto = random.randint(1, 10)
adivinado = False
intentos = 0

while not adivinado:
    intentos += 1
    guess = int(input("Adivina el número (entre 1 y 10): "))
    if guess == numero_secreto:
        adivinado = True
        print(f"¡Felicidades, has adivinado el número secreto en {intentos} intentos!")
    elif guess < numero_secreto:
        print("El número secreto es mayor. ¡Inténtalo de nuevo!")
    else:
        print("El número secreto es menor. ¡Inténtalo de nuevo!")

