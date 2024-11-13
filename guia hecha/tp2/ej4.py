import random

def eliminarElementos():
    lista1 = []
    lista2 = []
    for i in range(30):
        aux = random.randint(1,50) 
        lista1.append(aux)
    for i in range(30):
        aux = random.randint(1,50) 
        lista2.append(aux)

    print("Primera lista de enteros", lista1)

    print("Segumda lista de enteros", lista2)

    print("Lista 1 sin los elementos que aparecen en lista 2 ")

    for i in range(30): 
        if lista2[i] in lista1: 
            aux = lista2[i]
            lista1.remove(aux)

    print(lista1)



eliminarElementos()