"""
Consiste en funciones que se llaman a sí mismas
evitando estructuras iterativas
def recursivo(...):
    ...
    recursivo(...):
    ...

Identificar Caso Base:
Para su solución no requiere utilizar la función que se está definiendo.
Identificar Casos Recursivos:
Para su solución requiere llamarse a sí misma

Las definiciones recursivas funcionan siempre y cuando las llamadas recursivas en algún momento lleguen a los casos base.

Ejemplo didáctico:
Calcular la suma de los N primeros números naturales.
Calcular 1+2+3+…+N
def sumaNaturales(n):
    suma=0
    for cont in range(n+1):
        suma=suma+cont
    return suma

def sumaNaturalesRecursivo(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    else:
        return n + sumaNaturalesRecursivo(n-1)

Toda función recursiva puede ser resuelto utilizando ciclos y viceversa.        

funciones recursivas sin retorno
Desarrollar una función para mostrar una cuenta regresiva desde N por pantalla.
def cuentaRegresivaIterativa(n):
    for i in range(n,0,-1):
        print(i)

def cuentaRegresivaRecursiva(n):
    if n==0:
        print("0")
    else:
        print(n)
        cuentaRegresivaRecursiva(n-1)

funciones recursivas con retorno
Desarrollar una función para calcular el factorial de un número.
def factorialIterativo(n):
    if n<0:
        factorial = -1
    else: 
        factorial=1
        for cont in range(1, n+1):
            factorial=factorial*cont
    return factorial

def factorialRecursivo(n):
    if n<0:
        return -1
    elif n==0 or n==1:
        return 1
    else:
        return n*factorialRecursivo(n-1)

Un algoritmo recursivo no es mejor que uno iterativo,
ni viceversa. En cada situación será conveniente
analizar cuál algoritmo provee la solución al
problema de forma más clara y eficiente.

Funciones recursivas con retorno
Recorrer una lista con indices
Desarrollar una función para sumar los elementos de una lista
def sumaElementosIterativa(lista):
    suma=0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def sumaElementosRecursivo(lista, i=0): #en cada llamada la variable i esta indicando cual elemento analizar
    if i == len(lista):
        return 0
    else:
        return lista[i] + sumaElementosRecursivo(lista, i+1)


Funciones recursivas con retorno
Recorrer una lista con rebanadas
Desarrollar una función para sumar los elementos de una lista
def sumaElementosRecursivo(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumaElementosRecursivo(lista[1:]) 

#return lista[0]: cada llamada a la funcion analiza o toma el primer elemento
#sumaElementosRecursivo(lista[1:]): se llama de nuevo sin ese element ya analizado.

Funciones recursivas con retorno
Comparar elementos lista
Desarrollar una función para determinar si esta ordenada en forma ascendente
def ordenadaAscendenteIterativa(lista):
    i=0
    while i<len(lista) -1 and lista[i] < lista[i+1]:
        i +=1
    if i == len(lista)-1:
        return True
    else: 
        return False

def ordenadaAscendenteRecursiva(lista):
    if len(lista) < 2:
        return True
    else:
        if lista[0] < lista[1]:
            return ordenadaAscendenteRecursiva(lista[1:])
        else:
            return False

Funciones recursivas con retorno
Analizar una cadena
Desarrollar una función para contar cuantas vocales posee una cadena.
def contarVocalesIterativa(cad):
    cont=0
    for letra in cad:
        letra = letra.lower()
        if letra in ['a','e','i','o','u']:
            cont += 1
        else:
            cont += 0
    return cont

def contarVocalesRecursivo(cad):
    if len(cad) == 0:
        return 0
    else:
        letra = cad[0].lower()
        if letra in ['a','e','i','o','u']:
            return 1 + contarVocalesRecursivo(cad[1:])
        else:
            return 0 + contarVocalesRecursivo(cad[1:])

Funciones recursivas con retorno
Analizar una matriz
Desarrollar una función para contar cuantas veces aparece un numero en una matriz.
def contarIterativo(matriz,valor):
    cont = 0
    for fila in matriz:
        cont += fila.count(valor)
    return cont

def contarRecursivo(matriz, valor):
    if len(matriz) == 0:
        return 0 
    else:
        return matriz[0].count(valor) + contarRecursivo(matriz[1:], valor)

def contarIterativo(matriz, valor):
    cont=0
    suma=0
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] == valor:
                cont += 1
    return cont

def contarRecursivo(matriz, valor, f=0):
    if f == len(matriz):
        return 0
    else:
        sumaFila=0
        for c in range(len(matriz[f])):
            if matriz[f][c] == valor:
                sumaFila += 1
        return sumaFila + contarRecursivo(matriz, valor, f+1)

"""
