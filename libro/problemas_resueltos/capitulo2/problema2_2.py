P = int(input("Ingresa un valor entero:"))
Q = int(input("Ingresa otro valor entero:"))
EXP = P**3 + Q**4 - 2*P**2
if EXP < 680:
    print("Sus valores cumplen con la expresion dada")
    print(f"Sus valores son: {P} y {Q}")
print("Fin del programa")
