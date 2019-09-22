RADIO = float(input("Ingresa el radio del cilindro:"))
ALTU = float(input("Ingresa la altura del cilindro:"))
VOL = 3.141592 * (RADIO ** 2) * ALTU
ARE = 2 * 3.141592 * RADIO * ALTU
print(f"El volúmen del cilindro ingresado es {VOL} y el área de éste mismo es {ARE}")
