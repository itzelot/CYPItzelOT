tipoenf = int(input("Ingresa el tipo de enfermedad del paciente:"))
edad = int(input("Indica la edad del paciente:"))
dias = int(input("Indica el numero de dias que el paciente estuvo hospitalizado:"))
if tipoenf == 1:
    costot = dias*25
    print(f"Costo Total: ${costot}")
elif tipoenf == 2:
    costot = dias*16
    print(f"Costo Total: ${costot}")
elif tipoenf == 3:
    costot = dias*20
    print(f"Costo Total: ${costot}")
elif tipoenf == 4:
    costot = dias*32
    print(f"Costo Total: ${costot}")

if edad >= 14:
    if edad <= 22:
        costot = costot*1.10
        print(f"Costo Total: ${costot}")

print("FIN DEL PROGRAMA")
