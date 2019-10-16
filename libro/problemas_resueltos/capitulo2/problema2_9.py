prebas = float(input("Ingresa el precio basico del producto: $"))
if prebas > 500:
    imp = 20*0.30 + (prebas-40)*0.50
    pretot = prebas+imp
    print(f"El impuesto es de: ${imp}")
    print(f"El costo total del producto es de: ${pretot}")

else:
    if prebas > 40:
        imp = 20*0.30 + (prebas-40)*0.40
        pretot = prebas+imp
        print(f"El impuesto es de: ${imp}")
        print(f"El costo total del producto es de: ${pretot}")

    else:
        if prebas > 20:
            imp = (prebas-20)*0.30
            pretot = prebas+imp
            print(f"El impuesto es de: ${imp}")
            print(f"El costo total del producto es de: ${pretot}")

        else:
            imp = 0
            pretot = prebas+imp
            print(f"El impuesto es de: ${imp}")
            print(f"El costo total del producto es de: ${pretot}")

print("FIN DEL PROGRAMA")
