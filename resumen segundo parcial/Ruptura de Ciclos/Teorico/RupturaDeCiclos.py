#Estructura iterativa: instruccion
#BREAK - CONTINUE
"""
Existen instrucciones que rompen la ejecucion de un ciclo:
While / For
BREAK - CONTINUE
"""


#CONTINUE:
"""
El uso de esta instrucción en una iteración, finaliza la iteración y comienza la siguiente.
Puede utilizarse las veces que sea necesario dentro de un ciclo.

Ejercicio 1: Desarrollar una funcion para sumar los digitos pares.

#OPCION 1:

def sumaDigitosPar2(nro):
    suma=0
    for digito in str(abs(nro)):
        if int (digito)%2!=0:
            continue #cuando se cumple la condicion salta a la siguiente iteracion
        suma += int(digito)
    return suma

#OPCION 2:

def sumaDigitosPar2(nro):
    suma=0
    if nro <0:
        nro = nro*(-1)
    while nro > 0:
        digito = nro %10
        nro=nro//10
        if digito%2!=0:
            continue
        suma=suma+digito
    return suma

"""


#BREAK:
"""
El uso de esta instrucción en una iteración, finaliza por completo el ciclo.
Puede utilizarse las veces que sea necesario dentro de un ciclo.

Ejercicio 1: Desarrollar una función para determinar si un numero es primo

def esPrimo(numero):
    "Retorna True si el numero es primo, False caso contrario."
    if numero<=0:
        return False
    primo = True

    for divi in range(2, numero):
        if numero%divi==0:
            primo=False
            break #cuando se cumple la condicion se termina el ciclo.

    return primo

"""

#FOR-ELSE:
"""
La estructura for Puede tener un else asociado.
Se ejecuta si el for finaliza de manera «normal».
Normal : cuando termine de recorrer todos los iterables.
"""

#WHILE-ELSE:
"""
La estructura while Puede tener un else asociado.
Se ejecuta si el while finaliza de manera «normal».
Normal : cuando su condición resulte falsa.

EJEMPLO:

lista = [3,23,45,18,32,8]
nro=int(input("ingrese un numero a buscar: "))
i=0
while i<len(lista):
    if nro==lista[i]:
        print("El nro se encontro en la ubicacion", i)
        break
    i = i +1
else:
    print("El nro no se encontro")

"""

#WHILE TRUE: CICLO INFINITO
"""
Es un bucle infinito a menos que exista una condición para terminarlo dentro del bloque iterativo.

while True:
    #...
    if [condicion] == False:
        break
        
#Si no existiera la condición de terminación, se ejecuta en forma indeterminada

EJEMPLO 1:
suma=0
while True:
    nro=int(input("Ingrese un numero: "))
    if nro == -1:
        break
    suma=suma+nro
print("La suma es: ", suma)

#IMPORTANTE: Utilizar while True para emular un ciclo for es una mala práctica de programación.
i=0
while True:
    if i>=10:
        break
    print(i)
    i += 1

for i in range(10):
    print(i)


"""

