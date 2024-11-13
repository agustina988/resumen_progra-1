def maximo(n1,n2,n3): 
    lista = [n1,n2,n3]
    mayor = False
    for i in range(0,2): 
        for j in range(0,2):
            if lista[i] > lista[j]: 
                mayor = True
                num_mayor = lista[i]
            #elif lista[i] == lista[j]: 
            #    mayor = False
            else: 
                mayor = False

    return mayor, num_mayor


n1 = int(input("Ingrese "))

n2 = int(input("Ingrese "))

n3 = int(input("Ingrese "))

invocar = maximo(n1,n2,n3) 

print(invocar)