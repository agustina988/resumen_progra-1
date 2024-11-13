import random 

def filtro(numero): 
    if numero % 2 != 0: 
        return True

def generarListaRandom():
    lista1 = []
    for i in range(50): 
        lista1.append(random.randint(1,100))
    return lista1

numeros = generarListaRandom()

print(list(filter(filtro,numeros)))

