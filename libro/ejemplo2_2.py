SUE = float(input("Ingresa tu sueldo:"))
AUM = SUE * 0.15
NSUE = SUE + AUM
if SUE < 1000:
    print(f"Adquiere un aumento del 15%") 
    print(f"Su sueldo es de: ${NSUE}")
print("Fin del programa")

