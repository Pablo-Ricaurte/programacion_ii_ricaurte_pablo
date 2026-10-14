print("=== CONTROL DE ENERGIA===")
energia_text= "ochenta"
try:
    energia = int("mucho")
    print(energia)
except ValueError:
    print("Error : debe ser numerico")

print("Fin del sistema")

"""
ValueError
TypeError
keyError
IndexError
ZeroDivision
"""

def calcular_energia(total, cantidad):
    try:
        resultado = total / cantidad
        return resultado
    except ZeroDivisionError as error:
        print("Error: division entre cero", error)
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1: ", calcular_energia(100,4))
print("Caso 2: ", calcular_energia(100/0))
print("Caso 3:", calcular_energia(100, "cautro"))

print("=== DIAGNOSTICO R2-D2 ===")
try:
    energia = int(90)
    print("Energia ", energia)
except ValueError:
    print("Error de lectura")
else:
    print("Diagnostico completado")
finally:
    print("Cerrando diagnostico")

def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser numero entero")
    if energia < 0 or energia > 100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return energia

try:
    resultado = validar_energia(150)
    print("Energia", resultado)
except(TypeError, ValueError) as error:
    print("Error: ", error)

