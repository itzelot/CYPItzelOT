may = -100000
men = 100000
n = int(input("Indica el numero de enteros que se ingresan:"))
for i in range(1,n,1):
    num = int(input("Ingresa un numero entero:"))
    if num > may:
        may = num
    else:
        if num < men:
            men = num
print(f"El numero mayor es: {may}")
print(f"El numero menor es: {men}")
print("FIN DEL PROGRAMA")
