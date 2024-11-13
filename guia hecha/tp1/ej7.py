def verSiEsBisiesto(año): 
    flag = False
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): 
        flag =  True
    return flag

def verificarFecha(dia,mes): 
    valido = False
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]

    if dia <= dias[mes-1]: 
        valido = True
        
    return valido

def verificarLimite(mes,año): 
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    limite = dias[mes-1]
    corroborarAñoBisiesto = verSiEsBisiesto(año)
    if mes == 2 and corroborarAñoBisiesto == True: 
        limite +=1
    return limite

def diaSiguiente(dia,mes,año): 
    limite = verificarLimite(mes,año) 
    if dia + 1 > limite: 
        if mes + 1 > 12: 
            mes = 1
            año += 1
            dia = 1
        else:
            mes += 1
            dia = 1
    else: 
        dia += 1

    return dia,mes,año

def programaDiaSiguiente():
    validacion = False
    while validacion == False: 

        dia = int(input("ingrese el dia "))
        while dia < 1 or dia > 31: 
            dia = int(input("ingrese bien el dia "))  
        
        mes = int(input("ingrese el mes "))
        while mes < 1 or mes > 12: 
            mes = int(input("ingrese bien el mes "))  

        año = int(input("ingrese el año "))
        while año < 1000 or año > 2024: 
            año = int(input("ingrese bien el año "))
        
        corroborar = verificarFecha(dia,mes)
        if corroborar == True: 
            validacion = True
    
    siguienteDia = diaSiguiente(dia,mes,año)
    print(siguienteDia)

# programaDiaSiguiente() # quitar comentario al inicio para hacer funcionar programa

def sumarNDias(dia,mes,año,diasSumar):
    diasSumados = 0
    limite = verificarLimite(mes,año) 
    while diasSumados < diasSumar:
        if (dia + 1) > limite: 
            if mes + 1 > 12: 
                mes = 1
                año += 1
                dia = 1
            else:
                mes += 1 
                dia = 1

            limite = verificarLimite(mes,año)
        else: 
            dia += 1

        diasSumados += 1
    
    return dia,mes,año

def programaSumarNDias():
    validacion = False
    while validacion == False: 

        dia = int(input("ingrese el dia "))
        while dia < 1 or dia > 31: 
            dia = int(input("ingrese bien el dia "))  
        
        mes = int(input("ingrese el mes "))
        while mes < 1 or mes > 12: 
            mes = int(input("ingrese bien el mes "))  

        año = int(input("ingrese el año "))
        while año < 1000 or año > 2024: 
            año = int(input("ingrese bien el año "))
        
        corroborar = verificarFecha(dia,mes)
        if corroborar == True: 
            validacion = True
    
    diasSumar = int(input("ingrese cuantos dias quiere sumar "))
    while diasSumar < 1: 
        diasSumar = int(input("ingrese al menos 1 dia para sumar "))

    sumaDias = sumarNDias(dia,mes,año,diasSumar)
    print(sumaDias)

# programaSumarNDias() # quitar comentario al inicio para hacer funcionar programa