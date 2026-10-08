valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("Tabla de multiplicar del 5:")
multiplicador = 5
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)

print("Area de un triangulo: ", (5 * 10) / 2)

# Operadores de comparación:
""""
- == (igual)
- != (distinto)
< (menor)
- > (mayor)
- <= (menor o igual)
>= (mayor o igual)
"""""

velocidad_anakin = 950 
velocidad_sebulba = 900
print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual de rápido que Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es distinto de Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es más rápido o igual que Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es más lento o igual que Sebulba?", velocidad_anakin <= velocidad_sebulba)
resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type (resultado))

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("¿Todos los sistemas están funcionando?", motores_funcionando and escudos_funcionando)
print("¿Algunos sistemas están funcionando?", motores_funcionando or escudos_funcionando)
print("¿Los motores no están funcionando?", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible >= 50 and cantidad_alas >= 4)

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad = 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

# PRECENCIA DE OPERADORES
"""
1. ()
2. ** (potencia)
3./% (multiplicación, división, módulo)
4. (suma, resta)

"""

resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)

