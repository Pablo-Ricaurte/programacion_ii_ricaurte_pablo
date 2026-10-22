class Guerrero:
    nombre:str
    poder_inicial:int
    horas:int
    def __init__(self,nombre:str, poder_inicia:int, horas: int):
        self.nombre=nombre
        self.poder_inicial=poder_inicia
        self.horas=horas

    def atacar(self):
        print(f"{self.nombre} realiza ataque")

    def calcular_poder(self):
        return self.poder_inicial

class Goku(Guerrero):
    def __init__(self,nombre:str):
        super().__init__(nombre)
    def atacar(self):
        print(self.nombre, "Utiliza kamehameha")
    def calcular_poder(self):
        return self.poder_inicial + self.horas*100

class Vegeta(Guerrero):
    def __init__(self, nombre:str):
        super().__init__(nombre)