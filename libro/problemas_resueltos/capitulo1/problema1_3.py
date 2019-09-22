NOM = str(input("Indica el nombre del Dinosaurio:"))
PES = float(input("Indica el peso del Dinosaurio (en toneladas):"))
LON = float(input("Indica la longitud del Dinosaurio (en pies):"))
PESKIL = PES*1000
LONMET = LON*0.3047
print(f"El peso del Dinosaurio {NOM} en kilogramos es igual a: {PESKIL}kg, dado que el peso en toneladas es igual a {PES}")
print(f"La longitud del Dinosaurio {NOM} en metros es igual a: {LONMET}m, dado que la longitud en pies es igual a {LON}")
