"""-------------------------------------------------------------------------------------------------------------------------------"""

# Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
# rarios, y luego escribir un programa que las vincule:

# a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
# válida.
# b. Sumar N días a una fecha.
# c. Ingresar un horario desde teclado, verificando que sea correcto.
# d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
# segundo se considerará que el primero corresponde al día anterior. En ningún
# caso la diferencia en horas puede superar las 24 horas

"""---------------------------------------------------------------------------------------------------------------------------------"""

def ingrearEntero():
    while True:         
        try: 
            numero = int(input(" "))
            break
        except IOError: 
            print("Por favor ingrese un caracter valido ")

    return numero

def verSiEsBisiesto(ano): 
    flag = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
        flag =  True
    return flag

def verificarLimite(mes, ano):
    dias =(31,28,31,30,31,30,31,31,30,31,30,31)
    limite = dias[mes-1]
    corroborarAnoBisiesto = verSiEsBisiesto(ano)
    if mes == 2 and corroborarAnoBisiesto == True: 
        limite +=1
    return limite

"""------------------------------------------------------------------------------------------------------------------------------"""

# INGRESAR FECHA VALIDA
def ingresarFecha(): 
    print("Ingrese el dia ")
    dia = ingrearEntero()
    print("Ingrese el mes ")
    mes = ingrearEntero()
    print("Ingrese el ano")
    ano = ingrearEntero()

    dias = (31,28,31,30,31,30,31,31,30,31,30,31)
    fecha = None
    fechaValida = True
    if ano < 1000: 
        fechaValida = False
    else: 
        if mes < 1 or mes > 12: 
            fechaValida = False
        else: 
            if verSiEsBisiesto(ano) and mes == 2:
                if dia < 1 or dia > 29: 
                    fechaValida = False
            else: 
                if dia < 1 or dia > dias[mes]: 
                    fechaValida = False

    if fechaValida: 
        fecha = dia, mes, ano

    return fecha


#SUMAR DIAS A UNA FECHA
def sumarNDias(fecha):
    print("Ingrese cuantos dias quiere sumar ")
    diasSumar = ingrearEntero()
    dia, mes, ano = fecha
    diasSumados = 0
    limite = verificarLimite(mes,ano) 
    while diasSumados < diasSumar:
        if (dia + 1) > limite: 
            if mes + 1 > 12: 
                mes = 1
                ano += 1
                dia = 1
            else:
                mes += 1 
                dia = 1

            limite = verificarLimite(mes,ano)
        else: 
            dia += 1

        diasSumados += 1
    
    fecha = dia, mes, ano
    
    return fecha


#INGRESAR HORARIO 
def ingresarHorario(): 
    print("HORARIO 1: Ingrese una hora entre 0 y 23")
    hora1 = ingrearEntero()
    while hora1 < 0 or hora1 > 23: 
        print("Por favor ingrese un hora correcta")
        hora1 = ingrearEntero()

    print("Horario 2: ingrese una hora entre 0 y 23")
    hora2 = ingrearEntero()
    while hora2 < 0 or hora2 > 23: 
        print("Por favor ingrese una hora correcta")
        hora2 = ingrearEntero()

    print("HORARIO 1: Ingrese un minuto entre 0 y 59")
    minuto1 = ingrearEntero()
    while minuto1 < 0 or minuto1 > 59: 
        print("Por favor ingrese un minuto valido")
        minuto1 = ingrearEntero()

    print("HORARIO 2: Ingrese un minuto entre 0 y 59")
    minuto2 = ingrearEntero()
    while minuto2 < 0 or minuto2 > 59: 
        print("Por favor ingrese un minuto valido")
        minuto2 = ingrearEntero()

    #-----------------------------
    
    horario1 = hora1, minuto1
    horario2 = hora2, minuto2

    return horario1, horario2

#CALCULAR DIFERENCIA ENTRE DOS HORARIOS

def diferenciaHorarios(horario1, horario2): 
    hora1, minuto1 = horario1
    hora2, minuto2 = horario2
    difMin = 0
    difHora = 0
    dia = 0
    contador = 0

    if minuto2 > minuto1:
        contador = 0 
        while minuto2 != minuto1: 
            minuto2 -= 1
            contador += 1
            if minuto2 == 0: 
                minuto2 = 59
        difMin = contador
        print(difMin)
    else: 
        difMin = minuto1 - minuto2
    
    if hora2 > hora1: 
        dia += 1
        contador = 0
        while hora2 > hora1: 
            hora2 -= 1
            contador += 1
            #print(difHora)
        difHora = contador 
        diferenciaHoraria = dia, difHora, difMin
    else: 
        #print(difHora)
        difHora = hora1 - hora2
        diferenciaHoraria = difHora, difMin

    return diferenciaHoraria

#probando funcion a y b   
fecha = ingresarFecha()
print(fecha)
fechaSumada = sumarNDias(fecha)
print(fechaSumada)

#probando funcion c y d
horario1, horario2 = ingresarHorario()
print(horario1, horario2)
diferencia = diferenciaHorarios(horario1, horario2)
print("La diferencia entre los horarios es ", diferencia)