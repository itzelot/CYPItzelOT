n = int(input("Ingresa un numero entero que representa el numero de datos:"))
sumpos = 0
sumotr = 0
cuepos = 0
I = 1
for I in range(1,n,1):
    if I <= n:
        num = int(input("Ingresa un numero entero:"))
        if num > 0:
            sumpos += num
            cuepos += 1
            I += 1
        else:
            sumotr += num
            I += 1
progen = (sumpos + sumotr)/n
propos = (sumpos / cuepos)
print(f"El total de numeros positivos es:{cuepos}")
print(f"El promedio de ls numeros positivos es:{propos}")
print(f"El promedio general de los numeros es:{progen}")
print(f"FIN DEL PROGRAMA")
