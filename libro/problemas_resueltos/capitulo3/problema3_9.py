serie = 0
n = int(input("Ingresa el numero de terminos de la serie:"))
for i in range(1,n,1):
    serie += i ** i
print(f"{serie}")
print("FIN DEL PROGRAMA")
