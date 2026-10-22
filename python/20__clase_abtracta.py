from abc import ABC , abstractmethod

class NaveEspacial (ABC):
    modelo:str
    def __init__(self,modelo:str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass

class NaveCapsula(NaveEspacial):

    def __init__(self, modelo:str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo,"despegar con metores de capsula corp")

class NaveSaiyayin(NaveEspacial):
    def __init__(self, modelo:str):
        super().__init__(modelo)
    def despegar(self):
        print(self.modelo,"despegar inmediatamente")

nave_bulma =NaveCapsula("nave de bulma")
nave_vegeta=NaveSaiyayin("capsula saiyayin")
nave_bulma.despegar()
nave_vegeta.despegar()