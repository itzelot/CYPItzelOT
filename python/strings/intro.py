nombre = "Itzel Ortiz"
print(nombre)
print(nombre[0])
print(nombre[8])
print(nombre[-1])
print(nombre[-4])

#Slicing
print(nombre[1:3:1])

#valores por defecto de slicing
print(nombre[6::1])
print(nombre[::])#imprime toda la cadena
print(nombre[:5:])
print(nombre[:4:2])#de 2 en 2

#slicing negativo
print(nombre[-1:-8:-1])#sale al revés
print(nombre[::-1])#nombre al revés
print(nombre[-9:-14:-1])

frase="Solo existen 10 tipos de personas, las que saben binario y las que no"
print(frase[5:13:1])#Slicing para la palabra existen
print(frase[-37:-45:-1])#Slicing para palabra inversa
print(frase[::-1])#Slicing para farse inversa

print(dir(nombre))
print("Funciones de string(str)")
print(nombre.upper())
print(f"la palabra 'existen' esta en la posición:{frase.find('existen')}")
