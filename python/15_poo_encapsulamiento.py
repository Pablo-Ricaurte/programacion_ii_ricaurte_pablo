class CuentaZeni:
    titular: str
    __saldo: int
    
    def __init__(self):
        self.titula = self.titular
        self.__saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def retirar_dinero(self, cantidad: int):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado: ", cantidad)
        else:
            print("Retiro no permitido")

cuenta = CuentaZeni("Mr Satan", 5000)
print("Titular: ", cuenta.titular)
print("Saldo inicial: ", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("saldo final: ", cuenta.get_saldo())

