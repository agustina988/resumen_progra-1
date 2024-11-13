def ascendenteRecursivo(lista, i = 0): 
    if i == len(lista) -1: 
        return True
    
    if lista[i] > lista[i + 1]: 
        return False
    
    return ascendenteRecursivo(lista, i + 1)
    

lista = [1,2,3,4]
lista2 = [9,6,3,1]

check = ascendenteRecursivo(lista)

if check: 
    print("Lista ordenada de forma ascendente")
else: 
    print("Lista desordenada de forma ascendente")