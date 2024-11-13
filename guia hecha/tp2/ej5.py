def verificarAscendencia(lista): 
    ascendente = True
    for i in range(len(lista) -1): 
        if lista[i] > lista[i+1]: 
            ascendente = False
            break
    return ascendente

def programaPrincipal(): 
    lista1 = [1,2,3,4,5]
    lista2 = ['a','b','c','d','e']
    lista3 = [5,3,72,6,125]
    lista4 = ['g','a','r','x']
    chequear = verificarAscendencia(lista1)
    if chequear: 
        print("ordenada")
    else: 
        print("desordenada")

    chequear = verificarAscendencia(lista2)
    if chequear: 
        print("ordenada")
    else: 
        print("desordenada")

    chequear = verificarAscendencia(lista3)
    if chequear: 
        print("ordenada")
    else: 
        print("desordenada")

    chequear = verificarAscendencia(lista4)
    if chequear: 
        print("ordenada")
    else: 
        print("desordenada")

programaPrincipal()