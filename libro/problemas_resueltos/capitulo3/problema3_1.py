cuepar = 0
sumpar = 0
sumimp = 0
propar = 0
I = 1
for I in range(1,271,1):
    num = int(input("Ingresa un numero entero:"))
    if num % 2 == 0:
        sumpar += num
        cuepar += 1
        I += 1
        propar = sumpar/cuepar
    else:
        sumimp += num
        I += 1
print(f"El promedio es de:{propar}")
print(f"La suma impar es de:{sumimp}")
print("FIN DEL PROGRAMA")
