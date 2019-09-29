MAT = int(input("Matricula del alumno:"))
CAL1 = float(input("Ingresa la calificacion 1:")) 
CAL2 = float(input("Ingresa la calificacion 2:"))
CAL3 = float(input("Ingresa la calificacion 3:"))
CAL4 = float(input("Ingresa la calificacion 4:"))
CAL5 = float(input("Ingresa la calificación 5:"))
PRO = (CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO >= 6:
    print(f"Su promedio es de: {PRO}")
    print(f"{MAT}, APROBADO")
else:
    print(f"Su promedio es de: {PRO}")
    print(f"{MAT}, NO APROBADO")

