X1 = float(input("Ingresa el valor de la coordenada del eje x del Punto 1:"))
Y1 = float(input("Ingresa el valor de la coordenada del eje y del Punto 1:"))
X2 = float(input("Ingresa el valor de la coordenada del eje x del Punto 2:"))
Y2 = float(input("Ingresa el valor de la coordenada del eje y del Punto 2:"))
DIS = ((X1-X2)**2 + (Y1-Y2)**2)**0.5
print(f"La distancia entre los puntos P1 de coordenadas ({X1},{Y1}) y P2 de coordenadas ({X2},{Y2}) es de {DIS}")  
