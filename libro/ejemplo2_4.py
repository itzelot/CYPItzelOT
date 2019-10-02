SUE = float(input("Ingresa tu sueldo:"))
if SUE < 1000:
    NSUE = SUE * 1.15
    print("Tu aumento es del 15%")
    print(f"Tu sueldo es de: {NSUE}")
else:
    NSUE = SUE * 1.12
    print("Tu aumento es del 12%")
    print(f"Tu sueldo es de: {NSUE}")
print("Fin del programa")
