nom = 0
sue = float(input("ingresa el sueldo del empleado:"))
while (sue != -1):
    if sue < 1000:
        nsue = sue * 1.15
    else:
        nsue = sue * 1.12
    nom += nsue
    print(f"El nuevo sueldo del empleado es de:{nsue}")
print(f"El acumulo del nuevo sueldo de los trabajadores es de:{nom}")
print(f"FIN DEL PROGRAMA")
