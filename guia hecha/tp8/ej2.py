# Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año)
  
# y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido, OSEA: ej 12,10,30: 12 de Octubre de 2030

# La función debe contemplarse que el año se ingrese en dos digitos 

# los que serán interpretados según un año de corte definido dentro del
# programa. Cualquier año mayor que éste se considerará del siglo pasado. 

# ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
# para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
# 1931".

# Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
# cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
# mostrar el resultado

from time import sleep

def verSiEsBisiesto(ano): 
    flag = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
        flag =  True
    return flag

def tuplaToString(fecha):
    dia, mes, anio = fecha
    if len(str(anio)) == 2:
        if anio <= 35:
            anioString = "20" + str(anio)
        else:  
            anioString = "19" + str(anio)
    else:
        anioString = str(anio)

    meses = ("Enero", "Febrero", "Abril", "Marzo", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" )
        
    fechaExtendida = str(dia) + " " + meses[mes - 1] + " " + anioString
    return fechaExtendida

def validarFecha(fecha): 
    dia, mes, anio = fecha
    dias = (31,28,31,30,31,30,31,31,30,31,30,31)
    fecha = None
    fechaValida = True
    if len(str(anio)) > 4 or len(str(anio)) < 2 or len(str(anio)) == 3:
        fechaValida = False
    else:
        if len(str(anio)) == 2:
            pass
        else:
            if anio < 1000 or anio > 2100: 
                fechaValida = False
            else: 
                if verSiEsBisiesto(anio) and mes == 2:
                    if dia < 1 or dia > 29: 
                        fechaValida = False   
        if mes < 1 or mes > 12: 
            fechaValida = False
        else: 
            if dia < 1 or dia > dias[mes]: 
                fechaValida = False
    
    if fechaValida: 
        fecha = dia, mes, anio
    return fecha
    

def validarIngresoFecha():
    print("Ingrese la fecha que desea extender con formato dd, mm, aa")
    fechaValida = False
    while fechaValida == False:
        while True: 
            try:   
                dia = int(input("Dia: "))
                break
            except ValueError: 
                print("Por favor ingrese un entero ")
        while True: 
            try:
                mes = int(input("Mes: "))
                break
            except ValueError: 
                print("Por favor ingrese un entero ")
        while True: 
            try: 
                anio = int(input("Año: "))
                break
            except ValueError: 
                print("Ingrese un entero pro favor ")

        sleep(0.5)
        print("Validando datos...")
        sleep(1)
        fecha = dia, mes, anio
        fechaValidar = validarFecha(fecha)
        if fechaValidar != None:
            fechaValida = True
        else: 
            print("Fecha invalida, por favor vuelve a ingresasr")
    
    return fecha
        
        

fecha = validarIngresoFecha()
fechaExtentida = tuplaToString(fecha)
print("Su fecha extendida es", fechaExtentida)
