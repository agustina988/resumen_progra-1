def determinarCadenasCapicua(cadena):
    capicua = True
    for i in range(len(cadena) // 2):
        if i == 0:
            if cadena[i] != cadena[-1]: 
                capicua = False
         
        elif cadena[i] != cadena[-i -1]:
            capicua = False
    return capicua

cadena = input("Ingrese su cadena ")

check = determinarCadenasCapicua(cadena)

if check: 
    print("cadena capicua")
else: 
    print("cadena no capicua")