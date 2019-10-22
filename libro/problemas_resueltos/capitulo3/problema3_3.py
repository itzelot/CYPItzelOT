serie = 0
band = 'T'
I = 1
n = int(input("Ingresa el numero entero que representa el numero de terminos de la serie:"))
for I in range(1,n,1):
    if band == 'T':
        serie += 1/I
        band = 'F'
        I += 1
    else:
        serie -= 1/I
        band = 'T'
        I += 1
print(f"El resultado de los términos de la serie es:{serie}")
print("FIN DEL PROGRAMA")
