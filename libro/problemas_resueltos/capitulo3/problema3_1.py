cuepar = 0
sumpar = 0
sumimp = 0
I = 1
num = int(input("Ingresa un numero entero:"))
for I in range(1,num,271):
    if I <= 270:
        if num <> 0:
            if (-1**num)>0:
                 if num == 2*I:
                    cuepar += 1
                    sumpar = sumpar+(2*I)
                    print(f"{sumpar}")
            else:
                if num == (2*I)-1:
                    sumimp = sumimp+(2*I-1)
                    print(f"{sumimp}")
                
        


