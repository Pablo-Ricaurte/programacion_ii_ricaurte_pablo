naves = [
    "Caza n-1",
    "Nave real de Naboo",
    "transporte"
]

for nave in naves:
    print("inspecionando", nave)
print("inspeccion realizada")

rondas = range(1,6)

print("tipo de rondas: ", type(rondas))

for ronda in rondas:
    print(f"ronda de vigilancia: {ronda}")
    print(f"tipo de dato ronda: {type(ronda)}")

droides = range(1,17,2)
print("tipo de droides: ", type(droides))

for droide in droides:
    print(f"reparar droide B1 {droide}")
    print (f"tipo de dato droide: {type(droide)}")

planetas = [
    "Naboo",
    "Tatooine",
    "Coruscant"
]

recorrido = enumerate (planetas, start=5)
for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(posicion)}:{type (planeta)}")

paises = [
    "ecuador",
    "venezuela",
    "chile",
    "colombia",
    "Brasil",
    "Estados Unido"
]

for pais in paises:
    if pais == "chile":
        continue
    if pais == "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
jedi_activo = {
    "nombre": "Obi-wan",
    "fuerza": "120",
    "estilo_pelea": "samurai",
    "misiones": ["guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}

print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad=8, turbo_laser=2)
print(nave)

jedi["nombre"] = "Luke"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave}: {valor}")
