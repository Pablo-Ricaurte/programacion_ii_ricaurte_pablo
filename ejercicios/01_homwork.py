class AlmacenSemillas:
    __cantidad = int
    
    def __init__(self, cantidad):
        self.__cantidad = cantidad
        self.get_cantidad()
    
    def get_cantidad(self):
        print("Semillas disponibles: ", self.__cantidad)
    
    def set_cantidad(self, cantidad):
        if cantidad > 0:
            self.__cantidad = cantidad
            self.get_cantidad()
        else:
            print("La nueva cantidad debe ser mayor que 0")
    
    def entregar_semillas(self, cantidad):
        if self.__cantidad > cantidad:
            self.__cantidad -= cantidad
            self.get_cantidad()
        else:
            print(f"No se puede entregar {cantidad}, semillas disponibles: ", self.__cantidad)

semillas = AlmacenSemillas(10)
print("Se entrego 3 semillas a Goku")
semillas.entregar_semillas(3)

semillas.entregar_semillas(9)