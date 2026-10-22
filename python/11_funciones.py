def activar_sistema():
    print("== sistema de naboo ==")
    print("Sistema de control activado")

activar_sistema()

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe: {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")

mostrar_nave("caza N-1", 80)

def calcular_combustible(inicial, consumo):
    return inicial - consumo

print(f"combustible: {calcular_combustible(100, 25)}")

