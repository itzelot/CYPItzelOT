med = 0
chi = 0
gra = 0
n = int(input("Ingresa el numero de ventas:"))
for i in range(1,n,1):
    v = float(input("Ingresa el valor de la venta:"))
    if v <= 200:
        chi += 1
    else:
        if v < 400:
            med += 1
        else:
            gra += 1
print(f"El numero de ventas menores a $200 es de: {chi}")
print(f"El numero de ventas mayores a $200 pero menores a $400 es de: {med}")
print(f"El numero de ventas mayores a $400 es de: {gra}")
print("FIN DEL PROGRAMA")
