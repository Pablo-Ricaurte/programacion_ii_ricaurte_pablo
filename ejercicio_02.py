class RadarDragon:
    region1: int
    region2: int

    def __init__(self, region1:int, region2:int):
        self.region1 = region1
        self.region2 = region2
        self.buscar_esferas(region1, region2)

    def buscar_esferas(self, region1, region2):
        print(f"Se encontraron: {region1}, en la region 1\nfaltan: {7 - region1}")
        print(f"Se encontraron: {region2}, en la region 2\nfaltan: {7 - region1 - region2}")

radar_bulma = RadarDragon(3, 2)