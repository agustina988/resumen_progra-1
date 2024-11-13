""" 
12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron
"""


def ingresarSocios(): 
    sociosQueIngresaron = []
    numeroDeSocio = int(input("Ingrese su numero de socio, 0 para finaliar "))
    while numeroDeSocio != 0 and numeroDeSocio < 10000 or numeroDeSocio > 99999: 
        numeroDeSocio = int(input("Ingrese su numero de socio valido, 0 para finaliar  "))

    while numeroDeSocio != 0:
         
        sociosQueIngresaron.append(numeroDeSocio)
        
        numeroDeSocio = int(input("Ingrese su numero de socio, 0 para finaliar  "))
        while numeroDeSocio != 0 and numeroDeSocio < 10000 or numeroDeSocio > 99999: 
            numeroDeSocio = int(input("Ingrese su numero de socio valido, 0 para finaliar  "))
    
    return informarVecesIngreso(sociosQueIngresaron)

def informarVecesIngreso(sociosQueIngresaron): 
    for i in range(len(sociosQueIngresaron)): 
        cantidadDeveces = sociosQueIngresaron.count(sociosQueIngresaron[i])
        if cantidadDeveces > 1: 
            print("El socio ", sociosQueIngresaron[i], "ingreso un total de ",cantidadDeveces, "veces" )
        else: 
            print("El socio ", sociosQueIngresaron[i], "ingreso una vez")
    
    return darDeBaja(sociosQueIngresaron)


def darDeBaja(sociosQueIngresaron):
    ingresosEliminados = 0
    print("Registros de entrada actuales del club ", sociosQueIngresaron)
    numeroEliminar = int(input("Ingrese el numero de socio que desea eliinar "))
    while numeroEliminar in sociosQueIngresaron: 
        sociosQueIngresaron.remove(numeroEliminar)
        ingresosEliminados += 1
    print("Registros de entrada al club ahora, ",sociosQueIngresaron,"cantidad de ingresos eliminados ", ingresosEliminados)

ingresarSocios()