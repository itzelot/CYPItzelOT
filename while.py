otra= True
suma= 0.0
while(otra == True):
        cal = float(input("Calificacion:"))
        suma += cal
        otra = bool(int(input("Hay mas alumnos (0 No,1 Si):")))
print("Suma:", suma)
print("Fin del programa")
