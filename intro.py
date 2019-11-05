frase = "Sólo existen 10 tipos de personas, las que saben binario y las que no"
# hacer un slicing para imprimir la palabra existen
print(frase[5:13:1])

# hacer otro para imprimir la palabra personas en orden inverso
print(frase[-37:-45:-1])

#hacer un slicing que imprima toda la frase en orden inverso
print(frase[::-1])

print("Funciones de string")
print(frase.upper())
print(f"La palabra 'existen' está en la posición {frase.find('existen')}")
