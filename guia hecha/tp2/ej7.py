#intercalar listas con slicing 

lista1 = [1,2,3,4,5,6,7]
lista2 = ['A','B','C','D','E','F','G']

def intercalarListas(lista1,lista2):
    for i in range(len(lista1)):
    
        lista1[i*2:i*2] = lista2[i]
     

    print(lista1)

intercalarListas(lista1,lista2)