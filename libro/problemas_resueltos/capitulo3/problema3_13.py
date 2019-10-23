arsu = 0
arno = 0
mersu = 50000
mes = 0
arce = 0
for I in range(1,13,1):
    print(f"Mes: {I}")
    rno = float(input(f"Indica la lluvia caida en la region Norte en el mes:"))
    rce = float(input(f"Indica la lluvia caida en la region Centro en el mes:"))
    rsu = float(input(f"Indica la lluvia caida en la region Sur en el mes:"))
         
    arno += rno
    arce += rce
    arsu += rsu

    if rsu < mersu:
        mersu = rsu
        mes = I
prorce = arce / 12
print(f"Promedio de lluvia en la region centro:{prorce}")
print(f"Mes con menor lluvia en la region sur:{mes}")
print(f"Registro del mes con menor lluvia:{mersu}")

if arno > arce:
    if arno > arsu:
        print("La region con mayor lluvia es la region Norte")
    else:
        print("La region con mayor lluvia es la region Sur")
else:
    if arce > arsu:
        print("La region con mayor lluvia es la region Centro")
    else:
        print("La region con mayor lluvia es la region Sur")
print("FIN DEL PROGRAMA")
            
        
