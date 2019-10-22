sumser = 0
I = 2
band = 'T'
while (I <= 1800):
    sumser += 1
    print(f"El incremento del valor es:{I}")
    if band == 'T':
        band = 'F'
        I += 3
    else:
        band = 'T'
        I += 2
print(f"Los terminos de la serie son:{sumser}")
print("FIN DEL PROGRAMA")

