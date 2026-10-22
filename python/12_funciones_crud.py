flota = [
    {
        "N1-001": {
        "nombre": "Caza N-1",
        "Combustible": 80
        },
    },
    {
        "NR-002": {
        "nombre": "Nave Real",
        "Combustible": 35
        }
    }
]

def create_nave(nave):
    flota.append(nave)

def update_nave(nave_updated, index):
    flota[index].update[nave_updated]

def read_nave(index):
    return flota.pop(index)

def delete_nave(index):
    return flota.pop(index)

new_nave = {
    "Nr-003": {
        "nombre": "Nave Real 2",
        "combustible": 80
    },
}
create_nave(new_nave)
print(flota)
print(flota)

nave_updated = {
    "NR-006": {
        "Nombre": "Nave real NR6", 
        "combustible": 85
    }
}
update_nave(nave_updated, 2)
print(flota)
print(read_nave(2))
print(delete_nave(2))
print(flota)

