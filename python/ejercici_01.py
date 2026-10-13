peso = float(input("¿Cuál es el peso del paquete en kg?: "))
print("Zona 1 (América): $5 por kilo\nZona 2 (Europa): $7.5 por kilo\nZona 3 (Resto del mundo): $10 por kilo.")
zona = int(input("Seleccione la zona la que desea mandar el paquete: "))

if zona > 0 and zona < 4:
    if zona == 1:
        total = peso * 5
    elif zona == 2:
        total = peso * 7.5
    else:
        total = peso * 10
    print("El costo del envio es: ", total)
else:
    print("Error: seleccione una zona del 1-3, no realizo el calculo")