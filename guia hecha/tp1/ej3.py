def verificarDias(mes): 
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    diasMes = dias[mes]
    return diasMes

def calcularCostes(cantViajes):
    if cantViajes >= 1 and cantViajes < 21: 
        tarifa = cantViajes * 650 #* diasMes
    elif cantViajes > 20 and cantViajes <= 30:  
        tarifa = cantViajes * (650 * 0.80) #* diasMes
    elif cantViajes > 30 and cantViajes <= 40: 
        tarifa = cantViajes * (650 * 0.70) #* diasMes
    elif cantViajes > 40: 
        tarifa = cantViajes * (650 * 0.60) #* diasMes
    return tarifa

def programaPrincipal(): 

    #dia = int(input("ingrese el dia "))
    #while dia < 1 or dia > 31: 
    #    dia = int(input("ingrese el dia "))  
         
    #mes = int(input("ingrese el mes "))
    #while mes < 1 or mes > 12:  
    #    mes = int(input("ingrese el mes "))
        
    cantidadViajes = int(input("Ingrese la cantidad de viajes que relizara "))
    while cantidadViajes < 1: 
        cantidadViajes = int(input("Ingrese una cantidad de viajes valida "))    

    #cantidadDeDiasDelMes = verificarDias(mes)
    realizarCalculo = calcularCostes(cantidadViajes)
    print(realizarCalculo)

programaPrincipal()
