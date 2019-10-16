clave = int(input("Ingresa la clave de la zona geografica a la que se llamo:\n"))
numin = int(input("Ingresa la duracion (en minutos) de la llamada:"))
if clave == 12:
    cost= numin*2
elif clave == 15:
    cost= numin*2.2
elif clave == 18:
    cost = numin*4.5
elif clave == 19:
    cost = numin*3.5
elif clave == 23:
    cost = numin*6
elif clave == 25:
    cost = numin*6
elif clave == 29:
    cost = numin*5

print(f"El costo de la llamada es de: ${cost}")
print("FIN DEL PROGRAMA")
