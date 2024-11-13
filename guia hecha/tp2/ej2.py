import random

def listaRandom():
    lista = [] 
    cantidadElementos = int(input("ingresar "))
    for i in range(cantidadElementos): 
        lista.append(random.randint(1,100))
    print("lista original",lista)
    print(" ")
    return lista

def verificarElementosRepetidos(lista):
    repetidos = False 
    listaRepetidos = []
    for i in range(len(lista)): 
        aux = i 
        repetido = lista.count(aux)
        if repetido > 1: 
            repetidos = True
            listaRepetidos.append(aux)
    print("repetidos que aparecen en la lista ",listaRepetidos)
    print(" ")
    return repetidos

def crearListaElementosUnicos(lista):
    listaUnicos = []
    for i in range(len(lista)): 
        aux = i 
        repetido = lista.count(aux)
        if repetido > 1: 
            pass
        else: 
            listaUnicos.append(aux)
    return listaUnicos

def programaPrincipal(): 
    lista = listaRandom()
    verificar = verificarElementosRepetidos(lista)
    if verificar: 
        print("la lista contiene elementos repetidos")
    else: 
        print("la lista no contiene elementos repetidos ")
    listaUnicos = crearListaElementosUnicos(lista)
    print("lista de elementos unicos ",listaUnicos)

programaPrincipal()