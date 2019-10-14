CATE = int(input("Ingresa el numero de categoria (1 - 4):"))
SUE = float(input("Ingresa tu sueldo:"))
NSUE = 0

if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07

print(f"Tu nuevo sueldo es: ${NSUE} por tener la categoria {CATE}")
print("Fin del programa")
