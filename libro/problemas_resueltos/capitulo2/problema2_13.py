mat = int(input("Ingresa la matricula del alumno:"))
carr = str(input("Carrera en la que el alumno esta inscrito:"))
sem = int(input("Ingresa el numero de semestre que tiene aprobado el alumno:"))
prom = float(input("Ingresa el promedio del alumno:"))
if carr == "Economia":
    if sem >= 6:
        if prom >= 8.8:
            print(f"El alumno de matricula {mat} de la carrera {carr}, fue ACEPTADO")
elif carr == "Computacion":
    if sem > 6:
        if prom >= 8.5:
            print(f"El alumno de matricula {mat} de la carrera {carr}, fue ACEPTADO")
elif carr == "Contabilidad":
    if sem > 5:
        if prom > 8.5:
            print(f"El alumno de matricula {mat} de la carrera {carr}, fue ACEPTADO")
elif carr == "Administracion":
    if sem > 5:
        if prom > 8.5:
            print(f"El alumno de matricula {mat} de la carrera {carr}, fue ACEPTADO")

print("FIN DEL PROGRAMA")

