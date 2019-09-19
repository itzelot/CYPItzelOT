# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- Con la funcion format ()
4.- Es una variante de format()
"""

# 1.- Con comas, concatenar agregando
# un espacio y haciendo casting de tipo 
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad, nombre, estatura)

# 2.- con '+' hace lo mismo pero no
# realiza el casting automático
# no agrega espacios
print(str(edad) + str(estatura) + nombre)

# 3.- funcion format ()
print("Nombre: {} Edad: {} Estatura: {} ".format(nombre, edad, estatura))

# 4.- con una variante de format () simplificada
print(f"Nombre: \"{nombre}\" \nEdad:\t{edad}")

# print y el argumento end
print("Sólo hay 10 tipos de personas, las que saben binario y las que no",end="---")
print("otra línea")
