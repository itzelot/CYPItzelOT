compra = float(input("Ingresa el monto de la compra: $"))
if compra < 500:
    pagar = compra
    print(f"El total a pagar es de: ${pagar}")
else:
    if compra <= 1000:
        pagar = compra-(compra * 0.05)
        print(f"El total a pagar es de: ${pagar}")
    else:
        if compra <= 7000:
            pagar = compra-(compra * 0.11)
            print(f"El total a pagar es de: ${pagar}")
        else:
            if compra <= 15000:
                pagar = compra-(compra * 0.18)
                print(f"El total a pagar es de: ${pagar}")
            else:
                pagar = compra-(compra * 0.25)
                print(f"El total a pagar es de: ${pagar}")

print("FIN DEL PROGRMA")

