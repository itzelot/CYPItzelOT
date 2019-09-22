L1 = float(input("Ingresa la longitud del lado 1 del trángulo:"))
L2 = float(input("Ingresa la longitud del lado 2 del triángulo:"))
L3 = float(input("Ingresa la longitud del lado 3 del triángulo:"))
S = (L1 + L2+ L3)/2
AREA = (S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"EL área del triángulo dado es de: {AREA}")
