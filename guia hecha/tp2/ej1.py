import random

def cargarListasRandom(): 
    cantidadRandom = random.randint(10, 99)  
    listaRandom = [random.randint(1000,9999) for each in range(cantidadRandom)]
    print(listaRandom)
    return productoListaRandom(listaRandom)

def productoListaRandom(listaRandom):
    multiplicador = 1
    for i in range(len(listaRandom) -1): 
        multiplicador *= listaRandom[i]
        print(multiplicador,"\n")

def eliminarValorListaRandom(listaRandom):
    listaRandom = [1,23,3,23,23,23,23,23,23,432,543,23,543,24] 
    valorEliminar = int(input("Ingrese el valor que desea eliminar "))
    while valorEliminar in listaRandom: 
        listaRandom.remove(valorEliminar)
    print(listaRandom)

def determinarCapicua(supuestaListaCapicua):
    largo = len(supuestaListaCapicua) // 2
    print(largo)
    capicua = True

    for i in range(largo): 
        if supuestaListaCapicua[i] != supuestaListaCapicua[-(i+1)]: 
            capicua = False
            break

    if capicua == True: 
        print("si es")
    else:
        print("no es ")


#cargarListasRandom()
#eliminarValorListaRandom()
#lista = [17,50,90,50,17]
#determinarCapicua(lista)
