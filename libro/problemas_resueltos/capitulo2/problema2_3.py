A = float(input("Ingrese el valor de a (que no sea 0):"))
B = float(input("Ingrese el valor de b:"))
C = float(input("Ingrese el valor de c:"))
DIS = B**2-4*A*C
X1 = ((-B)+DIS**0.5)/2*A
X2 = ((-B)-DIS**0.5)/2*A
if DIS >= 0:
    print(f"Sus raíces reales son: X1={X1} Y X2={X2}")
print("Fin del programa")
