# Desarrollar una función que reciba tres números enteros positivos correspondientes 
# al día, mes, año de una fecha y verifique si corresponden a una fecha válida. 
# Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
# Devolver True o False según la fecha sea correcta o no.
# Realizar también un programa para verificar el comportamiento de la función.

import varios.verSiEsBisiesto as verSiEsBisiesto 

def verificarFecha(dia,mes,año): 
    print(dia,mes,año)
    valido = False
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(dias[mes])
    if dia <= dias[mes]: 
        valido = True
        
    return valido


def programaPrincipal(): 

    dia = int(input("ingrese el dia "))
    while dia < 1 or dia > 31: 
        dia = int(input("ingrese el dia "))  
         
    mes = int(input("ingrese el mes "))
    while mes < 1 or mes > 12: 
        mes = int(input("ingrese el mes "))      

    año = int(input("ingrese el año "))
    while año < 1000 and año > 2024: 
        año = int(input("ingrese el año "))

    verificar = verificarFecha(dia,mes,año)
    if verificar == True: 
        print('fecha valida')
    else: 
        print('fecha invalida')
        
programaPrincipal()