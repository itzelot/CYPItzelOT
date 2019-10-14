A = int(input("Ingresa un número entero:"))
B = int(input("Ingresa otro número entero:"))
C = int(input("Ingresa otro número entero:"))

if A < B:
    if B < C:
        print("Los números están en orden creciente")
    else:
        print("Los números no están en orden creciente")

else:
    print("Los números no están en orden creciente")

print("Fin del programa")
