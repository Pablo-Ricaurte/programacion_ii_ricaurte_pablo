"""
Control de Flota de Naboo
"""
naves = [
    {
        "nombre": "Caza N-1",
        "combustible": 80,
        "droides": ["R2-D2", "R2-A5"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 35,
        "droides": ["R2-N3"]
    },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droides": ["R2-D2", "R2-A5"]
    }
]

naves_lista = 0
naves_recarga = 0
total_droides = 0
total_ciclos = 0
ciclo = 0

for numero, nave in enumerate(naves, start=1):
    print(f"--- Nave : {numero} - {nave}")
    if nave["combustible"] >= 50:
        print("Estado inicial: LISTA")
        naves_lista += 1
    else:
        print("Estado inicial: RECARGA")
        naves_recarga += 1
        while nave["combustible"] <= 50:
            ciclo += 1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("Recarfa Completada")
        print("Estado Final: LISTA")
    total_droides += len(nave["droides"])
    for droide in nave["droides"]:
        print(f"droide : {droide}")
        
print("========================================")
print("RESUMEN")
print(f"total de naves: {len(naves)}")
print(f"naves en listas inicialmente: {naves_lista}")
print(f"naves en recarga: {naves_recarga}")
print(f"total de droides: {total_droides}")
print(f"total de ciclos: {total_ciclos}")