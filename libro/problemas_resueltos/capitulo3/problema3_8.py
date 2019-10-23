num = int(input("Comience con cualquier numero positivo:"))
if num > 0:
    while (num != 1):
        print(f"{num}")
        if (-1**num) > 0:
            num = num / 2
        else:
            num = (num * 3) + 1
else:
    print(f"{num} tiene que ser un entero positivo")
print("FIN DEL PROGRAMA")
