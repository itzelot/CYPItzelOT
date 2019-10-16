sue = float(input("Ingresa el sueldo basico del trabajador: $"))
cate = int(input("¿Cual es la categoria del trabajador? (1 - 8):"))
he = int(input("Ingresa el numero de horas extras:"))
if cate == 1:
    phe = 30
    print(f"El costo de la hora extra es de: ${phe}")
elif cate == 2:
    phe = 38
    print(f"El costo de la hora extra es de: ${phe}")
elif cate == 3:
    phe = 50
    print(f"El costo de la hora extra es de: ${phe}")
elif cate == 4:
    phe = 70
    print(f"El costo de la hora extra es de: ${phe}")
else:
    phe = 0
    print(f"El costo de la hora extra es de: ${phe}")


if he > 30:
    nsue = sue + 30*phe
    print(f"El sueldo a pagar del trabajador es de: ${nsue}")
else:
    nsue = sue + he*phe
    print(f"El sueldo a pagar del trabajador es de: ${nsue}")

print("FIN DEL PROGRAMA")
