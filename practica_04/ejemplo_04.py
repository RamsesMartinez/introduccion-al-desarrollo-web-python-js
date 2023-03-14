# Definición de la clase "CuentaBancaria"
class CuentaBancaria:
    # Constructor de la clase
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    # Método para obtener el saldo de la cuenta
    def obtener_saldo(self):
        return self.__saldo
    
    # Método para realizar un depósito en la cuenta
    def depositar(self, cantidad):
        self.__saldo += cantidad
    
    # Método para realizar un retiro de la cuenta
    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Error: Saldo insuficiente")
        else:
            self.__saldo -= cantidad

# Creación de un objeto a partir de la clase "CuentaBancaria"
mi_cuenta = CuentaBancaria("Juan", 500)

# Acceso al atributo privado "__titular" (genera un error)
print(mi_cuenta)
# print(mi_cuenta.__titular)

# Acceso al atributo privado "__saldo" mediante el método público "obtener_saldo"
print("El saldo de la cuenta es:", mi_cuenta.obtener_saldo())

# Realización de un depósito en la cuenta
mi_cuenta.depositar(500)

print("El saldo de la cuenta es:", mi_cuenta.obtener_saldo())


# Realización de un retiro de la cuenta
mi_cuenta.retirar(2000)
